from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url('contacts/', views.contacts, name='contacts'),
	url('about/', views.about, name='about')
]