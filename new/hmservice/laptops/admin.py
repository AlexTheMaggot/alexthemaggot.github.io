from django.contrib import admin

from laptops.models import LaptopBrand, LaptopModel

admin.site.register(LaptopBrand)
admin.site.register(LaptopModel)