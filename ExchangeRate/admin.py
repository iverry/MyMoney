from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ExchangeRate




class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('rate_date', 'usd2cny', 'hkd2cny')

admin.site.register(ExchangeRate, ExchangeRateAdmin)
