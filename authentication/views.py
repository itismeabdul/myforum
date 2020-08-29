from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from authentication import form

# Create your views here.

def login(request):
	if request.method == 'POST':
		#handle login here
		
		f = form.login(request.POST)
		
		if f.is_bound:
			if (f.is_valid) and (f.errors == {}):
				return HttpResponse(f.cleaned_data['userName'])
				
			else:
				return HttpResponse('Error! form invalid form!')
			
		else:
			return HttpResponse('Error! form empty')
		
	else:
		return render(request, 'login.html')
	
	
	
	
#sign up	
def signup(request):
	if request.method == 'POST':
		#handle login here
		
		f = form.signup(request.POST)
		
		if f.is_bound:
			if (f.is_valid) and (f.errors == {}):
				return HttpResponse(f.cleaned_data['firstName'])
				
			else:
				return HttpResponse('Error! form invalid form!')
			
		else:
			return HttpResponse('Error! form empty')
		
	else:
		return render(request, 'signup.html')
