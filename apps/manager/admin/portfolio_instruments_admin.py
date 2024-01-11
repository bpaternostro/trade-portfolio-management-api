from django.contrib import admin
from ..models import PortfolioFinancialInstrument

class PortfolioFinancialInstrumentAdmin(admin.ModelAdmin):
    list_display = ["portfolio", "status", "created_on"]

admin.site.register(PortfolioFinancialInstrument, PortfolioFinancialInstrumentAdmin)