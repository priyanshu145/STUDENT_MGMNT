from django.contrib import admin
from django.urls import path, include
from . import views



app_name = 'Admin'

urlpatterns = [
    path('add_student/', views.add_student , name='add_student')
    
]

