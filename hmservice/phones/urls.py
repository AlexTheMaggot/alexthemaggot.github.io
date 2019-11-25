from django.conf.urls import url
from django.urls import path

from phones.views import PhoneBrandListView, PhoneModelListView, PhoneModelDetailView
from phones.models import PhoneModel

urlpatterns = [
    path('', PhoneBrandListView.as_view(), name='phones'),
    path('Apple/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Apple')
    .order_by("-id")), name='Apple'),
    path('Apple/<slug:slug>/', PhoneModelDetailView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Apple')), name='Phonemodel'),
    path('Xiaomi/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Xiaomi')
    .order_by("-id")), name='Xiaomi'),
    path('Xiaomi/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('Samsung/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Samsung')
    .order_by("-id")), name='Samsung'),
    path('Samsung/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('Huawei/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Huawei')
    .order_by("-id")), name='Huawei'),
    path('Huawei/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('Google/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Google')
    .order_by("-id")), name='Google'),
    path('Google/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('Nokia/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Nokia')
    .order_by("-id")), name='Nokia'),
    path('Nokia/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('Sony/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Sony')
    .order_by("-id")), name='Sony'),
    path('Sony/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('Meizu/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Meizu')
    .order_by("-id")), name='Meizu'),
    path('Meizu/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('Asus/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Asus')
    .order_by("-id")), name='Asus'),
    path('Asus/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('HTC/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='HTC')
    .order_by("-id")), name='HTC'),
    path('HTC/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('Lenovo/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='Lenovo')
    .order_by("-id")), name='Lenovo'),
    path('Lenovo/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
    path('OnePlus/', PhoneModelListView.as_view(queryset=PhoneModel.objects.filter(brand__name__contains='OnePlus')
    .order_by("-id")), name='OnePlus'),
    path('OnePlus/<slug:slug>/', PhoneModelDetailView.as_view(), name='Phonemodel'),
]


