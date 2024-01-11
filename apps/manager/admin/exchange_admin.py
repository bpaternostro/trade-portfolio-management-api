from django.contrib import admin
from ..models import Exchange

class ExchangeAdmin(admin.ModelAdmin):
    list_display = ["name", "origin"]

admin.site.register(Exchange, ExchangeAdmin)