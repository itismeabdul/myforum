from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	
	else:
		return HttpResponseRedirect('/')
		
