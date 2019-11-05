from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url('contacts/', views.contacts, name='contacts'),
	url('about/', views.about, name='about'),
	url('wrong/', views.wrong, name='wrong'),
	url('thank-you/', views.thanks, name='thanks'),
]