from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path('Dashboard/', views.Dashboard , name = 'Dashbboard'),
    
]