from django.urls import path
from .views import FeedBackView, MainFeedBackView


urlpatterns = [
	path('', FeedBackView.as_view(), name='feedback_view'),
	path('main/', MainFeedBackView.as_view(), name='main_feedback_view')
]