from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Authentication'

urlpatterns = [
     path('Student_Login/' , views.Student_Login, name = 'Student_Login'),
     path('admin_login/', views.admin_login, name='admin_login')
    
]