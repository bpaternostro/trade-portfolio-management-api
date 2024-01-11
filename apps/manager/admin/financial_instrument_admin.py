from django.contrib import admin
from ..models import FinancialInstrument

class FinancialInstrumentAdmin(admin.ModelAdmin):
    list_display = ["name", "symbol", "type", "market"]
    list_filter = [
         "type",
         "market"
    ]
    search_fields = (
        "name",
        "symbol",
    )

admin.site.register(FinancialInstrument, FinancialInstrumentAdmin)