from django.core.management.base import BaseCommand, CommandError
from ...models import FinancialInstrument
from ...entry.mocked_data import FINANCIAL_INSTRUMENTS
from ...constants import Currency, Market, ApiSources

from ..core_methods import (
    _get_or_create_obj,
)


def _get_or_create_obj(klass, name, **kwargs):
    if not name:
        return None
    if len(klass.objects.filter(name=name)) == 0:
        kwargs["name"] = name
        obj = klass.objects.create(**kwargs)
        return obj
    return klass.objects.filter(name=name).first()


class Command(BaseCommand):
    help = "Imports balanz cedears data"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    # this is to get args from cmd
    #def add_arguments(self, parser):
    #    parser.add_argument('process_type', type=int)

    def handle(self, *args, **options):
        """ """
        for _item in FINANCIAL_INSTRUMENTS:
            
            ticker = _get_or_create_obj(
                FinancialInstrument,
                name=_item.get("name"),
                symbol=_item.get("symbol"),
                type=_item.get("type"),
                market=Market.ARGY if _item.get("type") else Market.CRIPTO,
                currency=Currency.ARGY if _item.get("type") else Currency.USD,
                price_source = ApiSources.BALANZ if _item.get("type") else ApiSources.COINBASE
            )
            
            ticker.save()