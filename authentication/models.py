from django.db import models

# Create your models here.

class users(models.Model):
	
	firstName = models.CharField(max_length=150, blank=True)
	
	lastName = models.CharField(max_length=150, blank=True)
	
	email = models.EmailField(blank=True)
	
	userName = models.CharField(max_length=150, blank=True)
	
	passWord = models.CharField(max_length=100, blank=True)
	
	AboutMe = models.CharField(max_length=200, blank=False)
	
	gender = models.CharField(max_length=10, blank=False)
	
	profilePicture = models.ImageField(upload_to='profilePictures/', blank=False)
	
	Activated = models.BooleanField(default=False)
	
	joined_on = models.DateTimeField(auto_now_add=True, blank=True)
	
	
	
	
	
	
	
	
	
	
