from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Review
from .views import ReviewView

urlpatterns = [
	path('', ListView.as_view(queryset=Review.objects.all().order_by("-date")[:20], 
		template_name="reviews/reviews.html")),
	path('new/', ReviewView.as_view(), name='review_new' )

]