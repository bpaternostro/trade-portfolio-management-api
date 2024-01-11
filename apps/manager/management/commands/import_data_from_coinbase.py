from django.core.management.base import BaseCommand
from ...models import FinancialInstrumentApiData, FinancialInstrument, FinancialInstrumentType
from ...services.coinbase import Coinbase
from ...constants import Status

from ..core_methods import (
    _get_or_create_obj,
)

def _get_or_create_obj(klass, **kwargs):
    obj = klass.objects.create(**kwargs)
    return obj

class Command(BaseCommand):
    help = "Imports coinbase data"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    # this is to get args from cmd
    #def add_arguments(self, parser):
    #    parser.add_argument('process_type', type=int)

    def handle(self, *args, **options):
        """ """
        coinbase = Coinbase()
        rates = coinbase.get_rates()
        coins_to_analyze = FinancialInstrument.objects.filter(type=FinancialInstrumentType.CRIPTO, status=Status.OPEN)
        coin_list = list(coins_to_analyze.values_list("symbol", flat=True))
        coins_to_process = {c["symbol"]:c for c in rates if c["symbol"] in coin_list}
        for c in coins_to_analyze:
            coin_rate = coins_to_process[c.symbol]
            ticker = _get_or_create_obj(
                FinancialInstrumentApiData,
                financial_instrument = c,
                actual_price = coin_rate["quote"]["USD"]["price"],
                actual_purchase_price = coin_rate["quote"]["USD"]["price"],
                actual_sell_price = coin_rate["quote"]["USD"]["price"],
                volume = coin_rate["quote"]["USD"]["volume_24h"],
                max = coin_rate["quote"]["USD"]["price"],
                min = coin_rate["quote"]["USD"]["price"],
                variation = coin_rate["quote"]["USD"]["percent_change_1h"],
                time = coin_rate["quote"]["USD"]["last_updated"],
            )
            
            ticker.save()