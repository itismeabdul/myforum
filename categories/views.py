from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def categories(request, cate):
	
	contex = {'group':cate}
	
	return HttpResponse(cate)
