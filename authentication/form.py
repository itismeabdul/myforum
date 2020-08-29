from django import forms

class login(forms.Form):
	userName = forms.CharField(max_length=10)
	
	passWord = forms.CharField(max_length=10)
	
	

class signup(forms.Form):
	firstName = forms.CharField(max_length=150)
	
	lastName = forms.CharField(max_length=150)
	
	email = forms.EmailField()
	
	userName = forms.CharField(max_length=100)
	
	passWord = forms.CharField(max_length=150)
	
	