from datetime import datetime

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .constants import ApiSources, Currency, FinancialInstrumentType, Market, PortfolioType, Status


# Create your models here.
class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BaseModelName(BaseModel):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Exchange(BaseModelName):
    origin = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Indicator(BaseModelName):
    status = models.IntegerField(choices = Status.choices, default=Status.OPEN)


class FinancialInstrument(BaseModelName):
    symbol = models.CharField(max_length=200)
    type = models.IntegerField(choices = FinancialInstrumentType.choices, default=FinancialInstrumentType.STOCK)
    market = models.IntegerField(choices = Market.choices, default=Market.ARGY)
    currency = models.IntegerField(choices = Currency.choices, default=Currency.ARGY)
    price_source = models.IntegerField(choices = ApiSources.choices, default=ApiSources.BALANZ)
    indicators = models.ManyToManyField(Indicator, blank=True)
    status = models.IntegerField(choices = Status.choices, default=Status.OPEN)

    def __str__(self):
        return self.name


class FinancialInstrumentApiData(BaseModel):
    financial_instrument = models.ForeignKey(FinancialInstrument, on_delete=models.CASCADE)
    actual_price = models.DecimalField(max_digits=10, decimal_places=5)
    actual_purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField(blank=True)
    max = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    min = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    variation = models.CharField(max_length=200, default=0)
    time = models.CharField(max_length=200)
    

class ExchangeFees(BaseModel):    
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    instrument = models.IntegerField(choices = FinancialInstrumentType.choices, default=FinancialInstrumentType.CRIPTO)
    fees = models.DecimalField(max_digits=10, decimal_places=6)  


class FinancialInstrumentIndicator(BaseModel):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    instrument = models.ForeignKey(FinancialInstrument, on_delete=models.CASCADE)
    value = models.DateTimeField(auto_now_add=False)


class Portfolio(BaseModelName):
    type = models.IntegerField(choices = PortfolioType.choices, default=PortfolioType.MONTHLY)
    tickers = models.ManyToManyField(FinancialInstrument, through="PortfolioFinancialInstrument", blank=True)
    status = models.IntegerField(choices = Status.choices, default=Status.OPEN)

    def __str__(self):
        return self.name


class PortfolioFinancialInstrument(BaseModel):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    ticker = models.ForeignKey(FinancialInstrument, on_delete=models.CASCADE)
    status = models.IntegerField(choices = Status.choices, default=Status.OPEN)
    buy_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    buy_date = models.DateField(blank=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class PortfolioFinancialInstrumentOperation(BaseModel):
    portofolio_financial_instrument = models.ForeignKey(PortfolioFinancialInstrument, on_delete=models.CASCADE)
    sell_quantity = models.IntegerField(default=0, blank=True)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    sell_date = models.DateField(blank=True, null=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class Trader(BaseModelName):
    portfolios = models.ManyToManyField(Portfolio, blank=True)

    def __str__(self):
        return self.name


"""def update_sell_date(sender, instance, **kwargs):
    if instance.sell_quantity and instance.sell_price:
        instance.sell_date = datetime.now()

    if instance.sell_quantity < instance.buy_quantity:
        quantity = instance.buy_quantity - instance.sell_quantity

        # Disconnect the signal temporarily to avoid recursion
        pre_save.disconnect(update_sell_date, sender=PortfolioFinancialInstrument)

        # Create the new instance
        PortfolioFinancialInstrument.objects.create(
            portfolio=instance.portfolio,
            ticker=instance.ticker,
            status=instance.status,
            buy_quantity=quantity,
            buy_price=instance.buy_price,
            buy_date=instance.buy_date
        )

        # Reconnect the signal
        pre_save.connect(update_sell_date, sender=PortfolioFinancialInstrument)

# Connect the signal
pre_save.connect(update_sell_date, sender=PortfolioFinancialInstrument)
"""