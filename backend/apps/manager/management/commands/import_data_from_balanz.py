from django.core.management.base import BaseCommand, CommandError
from ...models import FinancialInstrumentApiData, FinancialInstrument, FinancialInstrumentType
from ...services.balanz import Balanz
from ...constants import Status

from ..core_methods import (
    _get_or_create_obj,
)

def _get_or_create_obj(klass, **kwargs):
    obj = klass.objects.create(**kwargs)
    return obj

class Command(BaseCommand):
    help = "Imports balanz data"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    # this is to get args from cmd
    def add_arguments(self, parser):
        parser.add_argument('process_type', type=int)

    def handle(self, *args, **options):
        """ """
        balanz = Balanz()
        process_type = options.get("process_type")
        financial_type_label = FinancialInstrumentType.CEDEAR.label if process_type == 1 else FinancialInstrumentType.STOCK.label
        rates = balanz.get_rates(financial_instrument=financial_type_label)
        if not rates:
            raise CommandError(f'It was impossible to execute process type {process_type}')
        actives_to_analyze = FinancialInstrument.objects.filter(type=process_type, status=Status.OPEN)
        actives = list(actives_to_analyze.values_list("symbol", flat=True))
        actives_to_process = {c["ticker"]:c for c in rates if c["ticker"] in actives}
        for c in actives_to_analyze:
            coin_rate = actives_to_process[c.symbol]
            ticker = _get_or_create_obj(
                FinancialInstrumentApiData,
                financial_instrument = c,
                actual_price = coin_rate["u"],
                actual_purchase_price = coin_rate["pc"],
                actual_sell_price = coin_rate["pv"],
                volume = coin_rate["v"],
                max = coin_rate["max"],
                min = coin_rate["min"],
                time = coin_rate["t"],
            )
            
            ticker.save()