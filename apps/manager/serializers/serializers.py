from itertools import groupby
from django.conf import settings
from ..models import Portfolio, PortfolioFinancialInstrument, FinancialInstrumentApiData, ExchangeFees

from rest_framework import serializers



class PortfolioUpdateDataSerializer(serializers.ModelSerializer):
    current_price = serializers.SerializerMethodField()
    current_total = serializers.SerializerMethodField()
    variation = serializers.SerializerMethodField()
    variation_in_usd = serializers.SerializerMethodField()
    buy_fees = serializers.SerializerMethodField()
    sell_fees = serializers.SerializerMethodField()

    class Meta:
        model = PortfolioFinancialInstrument
        fields = ['ticker', 'status', 'current_price', 'buy_quantity', 'buy_price', 'buy_date', 'current_total', 'variation', 'variation_in_usd', 'sell_quantity', 'sell_price', 'sell_date', 'buy_fees', 'sell_fees']      

    def get_current_price(self, obj):
        return FinancialInstrumentApiData.objects.filter(financial_instrument=obj.ticker).latest('created_on').actual_price

    def get_current_total(self, obj):
        exchange_fees = ExchangeFees.objects.get(instrument=obj.ticker.type)
        result = 0
        if obj.buy_quantity:
            current_total = float(obj.buy_quantity * self.get_current_price(obj))
            result = current_total - float(current_total* float(exchange_fees.fees))
        return round(result)
    
    def get_total_buy(self, obj):
        exchange_fees = ExchangeFees.objects.get(instrument=obj.ticker.type)
        result = 0
        if obj.buy_price:
            current_total = float(obj.buy_quantity * obj.buy_price)
            result = current_total - float(current_total * float(exchange_fees.fees))
        return result
    
    def get_variation(self, obj):
        total_buy = self.get_total_buy(obj)
        return f'{round((self.get_current_total(obj) / total_buy) *100, 2)} %' if total_buy else 0
    
    def get_variation_in_usd(self, obj):
        total_buy = self.get_total_buy(obj)
        return round(self.get_current_total(obj) - total_buy, 2) if total_buy else 0
    
    def get_buy_fees(self, obj):
        exchange_fees = ExchangeFees.objects.get(instrument=obj.ticker.type)
        result = 0
        if obj.buy_price:
            current_total = float(obj.buy_quantity * obj.buy_price)
            result = float(current_total * float(exchange_fees.fees))
        return round(result)
    
    def get_sell_fees(self, obj):
        exchange_fees = ExchangeFees.objects.get(instrument=obj.ticker.type)
        result = 0
        if obj.sell_price:
            current_total = float(obj.sell_quantity * obj.sell_price)
            result = float(current_total * float(exchange_fees.fees))
        return result
    
    def to_representation(self, instance):
        response = super(PortfolioUpdateDataSerializer, self).to_representation(instance)
        if instance.ticker:
            response['ticker'] = instance.ticker.symbol
        return response

class PortfolioSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()
    
    class Meta:
        model = Portfolio
        fields = ["type", "status", "detail"]
        depth = 1

    def get_detail(self, obj):
        detail = PortfolioFinancialInstrument.objects.filter(portfolio=obj)
        return PortfolioUpdateDataSerializer(detail, many=True).data