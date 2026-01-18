from django.shortcuts import render

# Create your views here.

def Student_Login(request):
    return render(request, 'Authentication/Student_Login.html')


def admin_login(request):
    return render(request, 'Authentication/admin_login.html')
