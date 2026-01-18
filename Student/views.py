from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import StudentLoginForm

def Dashboard(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)

        if form.is_valid():
            roll = form.cleaned_data['roll']
            password = form.cleaned_data['password']

            user = authenticate(username=roll, password=password)

            if user:
                login(request, user)
                return redirect('Dashboard:Dashboard')
            else:
                form.add_error(None, "Invalid Roll Number or Password")
    else:
        form = StudentLoginForm()

    return render(request, 'Authentication/Student_Login.html', {'form': form})


