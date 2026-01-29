from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def index(request):
    
    return render(request, 'MAIN_APP/index.html')


def logout_views(request):
    logout(request)
    
    return render(request, 'MAIN_APP/index.html')
    
