from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('<slug:slug>/', views.dish_list, name='dish_list'),
]