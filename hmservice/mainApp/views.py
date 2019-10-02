from django.shortcuts import render

def index(request):
	return render(request, 'mainApp/index.html')

def contacts(request):
	return render(request, 'mainApp/basic.html', {'values': ['Phone number', '8(800)555-12-34',]})