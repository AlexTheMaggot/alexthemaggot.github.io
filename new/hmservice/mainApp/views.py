from django.shortcuts import render

def index(request):
	return render(request, 'mainApp/index.html')

def contacts(request):
	return render(request, 'mainApp/contacts.html')

def about(request):
	return render(request, 'mainApp/about.html')

def wrong(request):
	return render(request, 'feedback/wrong.html')
def thanks(request):
	return render(request, 'feedback/thanks.html')