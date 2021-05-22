from django.contrib import admin
from phones.models import PhoneBrand, PhoneModel

# Register your models here.

admin.site.register(PhoneBrand)
admin.site.register(PhoneModel)