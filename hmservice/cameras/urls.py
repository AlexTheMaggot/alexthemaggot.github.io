from django.conf.urls import url
from django.urls import path

from cameras.views import CameraBrandListView, CameraModelListView
from cameras.models import CameraModel

urlpatterns = [
    path('', CameraBrandListView.as_view(), name='cameras'),
    path('Apple/', CameraModelListView.as_view(queryset=CameraModel.objects.filter(brand__name__contains='Apple')
    .order_by("-id")), name='Apple'),
]


