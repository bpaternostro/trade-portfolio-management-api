from django.contrib import admin
from ..models import PortfolioFinancialInstrument

class PortfolioFinancialInstrumentAdmin(admin.ModelAdmin):
    list_display = ["ticker","portfolio", "status", "buy_quantity","created_on"]
    list_filter = [
         "portfolio",
    ]

admin.site.register(PortfolioFinancialInstrument, PortfolioFinancialInstrumentAdmin)