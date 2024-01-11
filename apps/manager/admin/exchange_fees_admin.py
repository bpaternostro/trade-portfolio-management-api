from django.contrib import admin
from ..models import ExchangeFees

class ExchangeFeesAdmin(admin.ModelAdmin):
    list_display = ["exchange", "instrument", "fees"]

admin.site.register(ExchangeFees, ExchangeFeesAdmin)