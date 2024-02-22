from django.contrib import admin
from ..models import FinancialInstrumentIndicator

class FinancialInstrumentIndicatorAdmin(admin.ModelAdmin):
    list_display = ["indicator", "instrument", "value"]

admin.site.register(FinancialInstrumentIndicator, FinancialInstrumentIndicatorAdmin)