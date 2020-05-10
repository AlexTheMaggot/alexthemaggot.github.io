from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('shop/', views.shop, name="shop"),
    path('order/', views.OrderView.as_view(), name='order')
]