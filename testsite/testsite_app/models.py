from django.db import models

# Create your models here.

class CarShop(models.Model):
    class Meta:
        verbose_name = "Car Shop"
        verbose_name_plural = "Car Shop"
    car_name = models.CharField(max_length=20)
    car_manufacturer = models.CharField(max_length=12)
    year_produce = models.CharField(max_length=4)