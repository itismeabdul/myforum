from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def content(request):
	return render(request, 'content.html')

# Create your views here.
