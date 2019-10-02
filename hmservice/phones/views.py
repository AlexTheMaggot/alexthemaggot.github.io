from django.shortcuts import render

def index(request):
	return render(request, 'phones/phones.html')