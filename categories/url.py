from django.urls import path, include
from categories import views

urlpatterns = [
	path('', views.categories, name='categories'),
]

