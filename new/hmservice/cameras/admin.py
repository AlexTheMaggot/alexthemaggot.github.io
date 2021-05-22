from django.contrib import admin

from cameras.models import CameraBrand, CameraModel


admin.site.register(CameraBrand)
admin.site.register(CameraModel)