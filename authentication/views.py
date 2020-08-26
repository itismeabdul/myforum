from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	
	elif request.method == 'POST':
		#handle login here
		return HttpResponseRedirect('/')
		
	else:
		return HttpResponseRedirect('/')
	
def signup(request):
		if request.method=='GET':
			return render(request,'signup.html')
		
		elif request.method =='POST':
			#handle sign up here
			return HttpResponseRedirect('/')
		
		else:
			return HttpResponseRedirect('/')
		
