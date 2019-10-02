from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from reviews.models import Review

urlpatterns = [
	url(r'^$', ListView.as_view(queryset=Review.objects.all().order_by("-date")[:20], 
		template_name="reviews/reviews.html")),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Review, template_name = "reviews/review.html"))
]