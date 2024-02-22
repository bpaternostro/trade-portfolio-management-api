from django.contrib import admin
from ..models import PortfolioFinancialInstrumentOperation

class PortfolioFinancialInstrumentOpAdmin(admin.ModelAdmin):
    list_display = ["portofolio_financial_instrument","sell_quantity", "sell_price"]

admin.site.register(PortfolioFinancialInstrumentOperation, PortfolioFinancialInstrumentOpAdmin)