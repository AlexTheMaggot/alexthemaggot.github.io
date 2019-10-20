from django.conf.urls import url
from django.urls import path

from tablets.views import TabletBrandListView, TabletModelListView
from tablets.models import TabletModel

urlpatterns = [
    path('', TabletBrandListView.as_view(), name='tablets'),
    path('Apple/', TabletModelListView.as_view(queryset=TabletModel.objects.filter(brand__name__contains='Apple')
    .order_by('-id')), name='Apple'),
]