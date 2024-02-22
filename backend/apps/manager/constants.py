import os

from django.db import models

class ApiSources(models.IntegerChoices):
    YAHOO = 0, ('Yahoo')
    BINANCE = 1, ('Binance')
    BALANZ = 2, ('Balanz')
    COINBASE = 3, ('Coinbase')


class Currency(models.IntegerChoices):
    ARGY = 0, ('Pesos')
    USD = 1, ('USD')


class FinancialInstrumentType(models.IntegerChoices):
    CRIPTO = 0, ('Cripto')
    CEDEAR = 1, ('Cedear')
    STOCK = 2, ('Stock')
    BONO = 3, ('Bono')
    CAUCION = 4, ('Caucion')
    FCI = 5, ('Fondo comun de inversion')


class Market(models.IntegerChoices):
    CRIPTO = 0, ('Cripto')
    ARGY = 1, ('Argy')
    NASDAQ = 2, ('Nasdaq')


class PortfolioType(models.IntegerChoices):
    WEEKLY = 0, ('Weekly')
    MONTHLY = 1, ('Monthly')
    LONG_TERM = 2, ('Long term')


class Status(models.IntegerChoices):
    OPEN = 0, ('Open')
    CLOSE = 1, ('Close')
    READY = 2, ('Ready')
    PENDING = 3, ('Pending')
    DELETE = 4, ('Delete')


BALANZ_URL = "https://clientes.balanz.com/api/v1"
BALANZ_INIT_URL = f'{BALANZ_URL}/auth/init?avoidAuthRedirect=true'
BALANZ_LOGIN_URL = f'{BALANZ_URL}/auth/login'
BALANZ_LOGOUT_URL = f'{BALANZ_URL}/logout'
BALANZ_COTIZACIONES_URL_CORE = f'{BALANZ_URL}/cotizaciones'
BALANZ_COTIZACIONES_URL = {
    "Cedear": f'{BALANZ_COTIZACIONES_URL_CORE}/cedears',
    "Stock": f'{BALANZ_COTIZACIONES_URL_CORE}/acciones/1'
}

HEADERS_COIN_MARKET_CAP = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': os.getenv("COINBASE_API_KEY"),
}

URL_COIN_MARKET_CAP = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

COINBASE_PARAMETERS = {
  'start':'1',
  'limit':'1000',
  'convert':'USD'
}
