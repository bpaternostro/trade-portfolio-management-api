import datetime

from django.conf import settings
from ..models import FinancialInstrument, Portfolio, PortfolioFinancialInstrument, FinancialInstrumentApiData, ExchangeFees, Trader, PortfolioFinancialInstrumentOperation
from django.db.models import F, Sum
from rest_framework import serializers

from ..services.helpers import get_currency_format

from ..constants import Status

class TraderSerializer(serializers.ModelSerializer):
    portfolios = serializers.SerializerMethodField()
    class Meta:
        model = Trader
        fields = ["id", "name", "created_on", "portfolios"]      
        depth = 1

    def get_portfolios(self, obj):
        portfolios = obj.portfolios.exclude(status__in=[Status.DELETE, Status.CLOSE])
        return PortfolioSerializer(portfolios, many=True).data

class CreatePortfolioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Portfolio
        fields = ["name", "type", "status"]


class FinancialInstrumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FinancialInstrument
        fields = ['id', 'symbol', 'type', 'market', 'currency', 'price_source', 'indicators', 'status']



class PortfolioDataSerializer(serializers.ModelSerializer):
    portfolio_updated = serializers.SerializerMethodField()

    class Meta:
        model = PortfolioFinancialInstrument
        fields = '__all__'

    def get_portfolio_updated(self, obj):
       portfolio = Portfolio.objects.get(id=obj.portfolio_id)
       return PortfolioSerializer(portfolio).data
        

class PortfolioCreateDataSerializer(PortfolioDataSerializer):

    class Meta:
        model = PortfolioFinancialInstrument
        fields = ['portfolio', 'ticker', 'status', 'buy_quantity', 'buy_price', 'buy_date', 'portfolio_updated'] 


class PortfolioUpdateDataSerializer(PortfolioDataSerializer):

    class Meta:
        model = PortfolioFinancialInstrument
        fields = ['status', 'buy_quantity', 'buy_price', 'buy_date', 'portfolio_updated']


class PortfolioFinancialInstrumentOperationSerializer(serializers.ModelSerializer):
    portfolio_updated = serializers.SerializerMethodField()
    
    class Meta:
        model = PortfolioFinancialInstrumentOperation
        fields = ["portofolio_financial_instrument", "sell_quantity", "sell_price", "sell_date", "portfolio_updated"]


    def get_portfolio_updated(self, obj):
       portfolio = Portfolio.objects.get(id=obj.portofolio_financial_instrument.portfolio_id)
       return PortfolioSerializer(portfolio).data

class PortfolioUpdateBulkDataSerializer(PortfolioDataSerializer):

    class Meta:
        model = PortfolioFinancialInstrument
        fields = ['status', 'portfolio_updated']


class PortfolioGetDetailDataSerializer(serializers.ModelSerializer):
    current_price = serializers.SerializerMethodField()
    current_total = serializers.SerializerMethodField()
    current_total_decimal = serializers.SerializerMethodField()
    variation = serializers.SerializerMethodField()
    variation_in_usd = serializers.SerializerMethodField()
    buy_fees = serializers.SerializerMethodField()
    total_buy = serializers.SerializerMethodField()
    #sell_fees = serializers.SerializerMethodField()
    buy_price_str = serializers.SerializerMethodField()
    available = serializers.SerializerMethodField()
    can_sell = serializers.SerializerMethodField()
    volume = serializers.SerializerMethodField()
    volume_diff = serializers.SerializerMethodField()

    class Meta:
        model = PortfolioFinancialInstrument
        fields = ['id', 'ticker', 'status', 'current_price', 'buy_quantity', 'buy_price', 'buy_price_str', 'buy_date', 'total_buy', 'current_total', 'current_total_decimal', 'variation', 'variation_in_usd', 'buy_fees', 'available', 'can_sell', 'volume', 'volume_diff']      
        depth = 1

        
    def get_buy_price_str(self, obj):
        return get_currency_format(obj.buy_price)
    
    def get_current_price(self, obj):
        return get_currency_format(FinancialInstrumentApiData.objects.filter(financial_instrument=obj.ticker).latest('created_on').actual_price)
    
    def get_current_price_decimal(self,obj):
        return FinancialInstrumentApiData.objects.filter(financial_instrument=obj.ticker).latest('created_on').actual_price
    
    def get_current_total_decimal(self, obj):
        exchange_fees = ExchangeFees.objects.get(instrument=obj.ticker.type)
        result = 0
        if obj.buy_quantity:
            current_total = float(obj.buy_quantity * self.get_current_price_decimal(obj))
            result = current_total - float(current_total* float(exchange_fees.fees))
        return round(result)
    
    def get_current_total(self, obj):
        return get_currency_format(self.get_current_total_decimal(obj))
    
    def get_total_buy_decimal(self, obj):
        exchange_fees = ExchangeFees.objects.get(instrument=obj.ticker.type)
        result = 0
        if obj.buy_price:
            current_total = float(obj.buy_quantity * obj.buy_price)
            result = current_total - float(current_total * float(exchange_fees.fees))
        return result
    
    def get_total_buy(self, obj):
        return get_currency_format(self.get_total_buy_decimal(obj))
    

    def get_total_sell_decimal(self, obj):
        exchange_fees = ExchangeFees.objects.get(instrument=obj.ticker.type)
        result = 0
        if obj.sell_price:
            current_total = float(obj.sell_quantity * obj.sell_price)
            result = current_total - float(current_total * float(exchange_fees.fees))
        return result
    
    def get_total_sell(self, obj):
        return get_currency_format(self.get_total_sell_decimal(obj))
    
    def get_variation(self, obj):
        total_buy = self.get_total_buy_decimal(obj)
        return f'{round((self.get_current_total_decimal(obj) / total_buy) *100, 2)} %' if total_buy else 0
    
    def get_variation_in_usd(self, obj):
        total_buy = self.get_total_buy_decimal(obj)
        return get_currency_format(round(self.get_current_total_decimal(obj) - total_buy, 2)) if total_buy else 0
    
    def get_buy_fees(self, obj):
        exchange_fees = ExchangeFees.objects.get(instrument=obj.ticker.type)
        result = 0
        if obj.buy_price:
            current_total = float(obj.buy_quantity * obj.buy_price)
            result = float(current_total * float(exchange_fees.fees))
        return get_currency_format(round(result))
    
    def get_available(self, obj):
        total_sell = PortfolioFinancialInstrumentOperation.objects.filter(portofolio_financial_instrument=obj.id).aggregate(Sum("sell_quantity"))
        total = total_sell.get("sell_quantity__sum")
        return (obj.buy_quantity - total) if total else obj.buy_quantity
    
    def get_can_sell(self, obj):
        available = self.get_available(obj)
        return available > 0
    
    def get_volume(self, obj):
        return float(FinancialInstrumentApiData.objects.filter(financial_instrument=obj.ticker).latest('created_on').volume)
    
    def get_volume_diff(self, obj):
        actual_volume = self.get_volume(obj)
        percentage =  actual_volume / FinancialInstrumentApiData.objects.filter(financial_instrument=obj.ticker).order_by('-created_on')[1].volume
        return f'{round(percentage *100, 2)} %' if actual_volume else 0
    

    #def get_sell_fees(self, obj):
    #    exchange_fees = ExchangeFees.objects.get(instrument=obj.ticker.type)
    #    result = 0
    #    if obj.sell_price:
    #        current_total = float(obj.sell_quantity * obj.sell_price)
    #        result = float(current_total * float(exchange_fees.fees))
    #    return get_currency_format(result)
    
    #def to_representation(self, instance):
    #    response = super(PortfolioGetDetailDataSerializer, self).to_representation(instance)
    #    if instance.ticker:
    #        response['ticker'] = instance.ticker.symbol
    #    return response
    

class PortfolioSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()
    last_update = serializers.SerializerMethodField()
    start_value = serializers.SerializerMethodField()
    actual_value = serializers.SerializerMethodField()
    performance = serializers.SerializerMethodField()
    difference = serializers.SerializerMethodField()
    
    class Meta:
        model = Portfolio
        fields = ["id", "name", "type", "status", "detail", "last_update", "start_value", "actual_value", "performance", "difference"]
        depth = 1

    def get_detail(self, obj):
        detail = PortfolioFinancialInstrument.objects.filter(portfolio=obj).exclude(status=Status.DELETE)
        return PortfolioGetDetailDataSerializer(detail, many=True).data if detail else []
    
    def get_last_update(self, obj):
        d = FinancialInstrumentApiData.objects.latest('created_on').created_on
        return d.strftime('%Y-%m-%d %H:%M:%S') 
    
    def get_start_value_decimal(self, obj):
        if not self.get_detail(obj):
            return 0
        
        total = PortfolioFinancialInstrument.objects.filter(portfolio=obj).exclude(status__in=[Status.DELETE]).annotate(
            total = F('buy_quantity') * F('buy_price')
        ).aggregate(Sum("total"))
        return total.get("total__sum")
    
    def get_start_value(self, obj):
        return get_currency_format(self.get_start_value_decimal(obj))
    
    def get_actual_value_decimal(self, obj):
        data = self.get_detail(obj)
        return sum([t.get("current_total_decimal") for t in data]) if data else 0
    
    def get_actual_value(self, obj):
        return get_currency_format(self.get_actual_value_decimal(obj))
    
    def get_performance(self, obj):
        actual_value = self.get_actual_value_decimal(obj)
        start_value = self.get_start_value_decimal(obj)
        if not start_value:
            return 0
        percentage =  actual_value / start_value
        return f"{percentage:.0%}"
    
    def get_difference(self, obj):

        return get_currency_format(self.get_actual_value_decimal(obj) - self.get_start_value_decimal(obj))
    
