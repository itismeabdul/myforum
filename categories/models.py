from django.db import models
from authentication.models import users

# Create your models here.
class post(models.Model):
	
	author = models.ForeignKey(users, models.SET_NULL,blank=True,null=True,)
	
	title = models.CharField(max_length=100, blank=True)
	
	body = models.TextField()
	
	created_on = models.DateTimeField(auto_now_add=True)
	
	category = models.CharField(max_length=100, blank=True)