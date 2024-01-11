from django.db import models
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
    buy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    buy_date = models.DateField(blank=True, null=True)
    sell_quantity = models.IntegerField(default=0, blank=True, null=True)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sell_date = models.DateField(blank=True, null=True)
