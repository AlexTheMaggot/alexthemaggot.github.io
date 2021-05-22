from django.urls import path

from tablets.views import TabletBrandListView, TabletModelListView, TabletModelDetailView
from tablets.models import TabletModel

urlpatterns = [
    path('', TabletBrandListView.as_view(), name='tablets'),
    path('Apple/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Apple')
    .order_by('-id')), name='Apple'),
    path('Apple/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('Samsung/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Samsung')
    .order_by('-id')), name='Samsung'),
    path('Samsung/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('Sony/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Sony')
    .order_by('-id')), name='Sony'),
    path('Sony/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('Lenovo/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Lenovo')
    .order_by('-id')), name='Lenovo'),
    path('Lenovo/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('Acer/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Acer')
    .order_by('-id')), name='Acer'),
    path('Acer/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('Asus/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Asus')
    .order_by('-id')), name='Asus'),
    path('Asus/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('Xiaomi/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Xiaomi')
    .order_by('-id')), name='Xiaomi'),
    path('Xiaomi/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('Huawei/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Huawei')
    .order_by('-id')), name='Huawei'),
    path('Huawei/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('Microsoft/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Microsoft')
    .order_by('-id')), name='Microsoft'),
    path('Microsoft/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('Dell/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Dell')
    .order_by('-id')), name='Dell'),
    path('Dell/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('HP/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='HP')
    .order_by('-id')), name='HP'),
    path('HP/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
    path('MSI/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='MSI')
    .order_by('-id')), name='MSI'),
    path('MSI/<slug:slug>/', TabletModelDetailView.as_view(), name='Tabletmodel'),
]