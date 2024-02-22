from django.contrib import admin
from ..models import Trader

class TraderAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Trader, TraderAdmin)