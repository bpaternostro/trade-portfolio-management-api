from django.contrib import admin
from ..models import FinancialInstrumentApiData

class FinancialInstrumentApiDataAdmin(admin.ModelAdmin):
    list_display = ["financial_instrument", "actual_price", "created_on"]
    list_filter = [
         "financial_instrument",
    ]
    search_fields = (
        "financial_instrument",
    )

admin.site.register(FinancialInstrumentApiData, FinancialInstrumentApiDataAdmin)