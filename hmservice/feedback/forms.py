from django import forms

from .models import MainFeedBack, FeedBack

class MainFeedBackForm(forms.ModelForm):
	class Meta:
		model = MainFeedBack
		fields = ['name', 'phone']

class FeedBackForm(forms.ModelForm):
	class Meta:
		model = FeedBack
		fields = ['name', 'phone', 'brand', 'model', 'serv']