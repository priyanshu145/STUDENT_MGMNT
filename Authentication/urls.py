from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Authentication'

urlpatterns = [
     path('Student_Login/' , views.Authentication, name = 'Student_Login'),
    
]