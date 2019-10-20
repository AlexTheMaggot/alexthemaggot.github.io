from django.urls import path

from laptops.views import LaptopBrandListView, LaptopModelListView
from laptops.models import LaptopModel

urlpatterns = [
    path('', LaptopBrandListView.as_view(), name='laptops'),
    path('Apple/', LaptopModelListView.as_view(queryset=LaptopModel.objects.filter(brand__name__contains='Apple')
    .order_by('-id')), name='Apple'),
]