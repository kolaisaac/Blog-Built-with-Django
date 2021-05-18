from django.contrib import admin
from .models import CarShop
# Register your models here.


class CarShopDB(admin.ModelAdmin):
    list_display = [
        "car_name","car_manufacturer","year_produce"
    ]

admin.site.register(CarShop, CarShopDB)