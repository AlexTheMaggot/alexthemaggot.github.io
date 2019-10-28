from django.conf.urls import url
from django.urls import path

from phones.views import PhoneBrandListView, PhoneModelListView, PhoneModelDetailView
from phones.models import PhoneModel

urlpatterns = [
    path('', PhoneBrandListView.as_view(), name='phones'),
    path('Apple/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Apple')
    .order_by("-id")), name='Apple'),
    path('Apple/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('Xiaomi/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Xiaomi')
    .order_by("-id")), name='Xiaomi'),
    path('Samsung/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Samsung')
    .order_by("-id")), name='Samsung'),
    path('Huawei/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Huawei')
    .order_by("-id")), name='Huawei'),
    path('Google/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Google')
    .order_by("-id")), name='Google'),
    path('Nokia/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Nokia')
    .order_by("-id")), name='Nokia'),
    path('Sony/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Sony')
    .order_by("-id")), name='Sony'),
    path('Meizu/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Meizu')
    .order_by("-id")), name='Meizu'),
    path('Asus/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Asus')
    .order_by("-id")), name='Asus'),
    path('HTC/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='HTC')
    .order_by("-id")), name='HTC'),
    path('Lenovo/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Lenovo')
    .order_by("-id")), name='Lenovo'),
    path('OnePlus/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='OnePlus')
    .order_by("-id")), name='OnePlus'),
]


