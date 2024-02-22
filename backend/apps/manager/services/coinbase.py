from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from .exchange import Exchange
from ..constants import HEADERS_COIN_MARKET_CAP, URL_COIN_MARKET_CAP, COINBASE_PARAMETERS, FinancialInstrumentType
from ..models import FinancialInstrumentApiData, FinancialInstrument

class Coinbase(Exchange):

    def __init__(self) -> None:
        self.session = None
        
    def _connect(self):
        # this is to connect to coinmarketcap
        self.session = Session()
        self.session.headers.update(HEADERS_COIN_MARKET_CAP)
    
    def get_rates(self):
        self._connect()
        try:
          response = self.session.get(URL_COIN_MARKET_CAP, params=COINBASE_PARAMETERS)
          coins_json = response.json()
          return coins_json["data"]
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)