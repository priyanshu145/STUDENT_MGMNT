from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Student.models import Student

@login_required
def add_student(request):

    # only admin allowed
    if not request.user.is_superuser:
        return render(request, 'error.html')

    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        password = request.POST['password']
        roll_no = request.POST['roll_no']
        email = request.POST['email']
        course = request.POST['course']

        # check username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'admin/add_student.html', {
                'error': 'Username already exists'
            })

        # create login user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        # create student profile
        Student.objects.create(
            user=user,
            full_name=full_name,
            roll_no=roll_no,
            email=email,
            course=course
        )

        return render(request, 'admin/add_student.html', {
            'success': 'Student added successfully'
        })

    return render(request, 'admin/add_student.html')
