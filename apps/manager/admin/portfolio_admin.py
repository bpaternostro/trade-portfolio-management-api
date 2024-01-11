from django.contrib import admin
from ..models import Portfolio, PortfolioFinancialInstrument

class PortfolioFinancialInstrumentAdmin(admin.TabularInline):
    model = PortfolioFinancialInstrument
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["name", "created_on", "type", "status"]
    inlines = [
        PortfolioFinancialInstrumentAdmin
    ]

admin.site.register(Portfolio, PortfolioAdmin)