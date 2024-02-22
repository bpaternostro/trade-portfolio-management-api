from django.contrib import admin
from ..models import Indicator

class IndicatorAdmin(admin.ModelAdmin):
    list_display = ["name", "status"]

admin.site.register(Indicator, IndicatorAdmin)