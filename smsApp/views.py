from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


User = get_user_model()

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

'''def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        errors = []

        if not (username and firstname and lastname and email and phone and password and confirm_password ):
            errors.append('All fields are required.')
        if password != confirm_password:
            errors.append('Passwords do not match.')
        if User.objects.filter(username=username).exists():
            errors.append('Username is already taken.')
        if User.objects.filter(email=email).exists():
            errors.append('Email is already registered.')

        if errors:
            return JsonResponse({'errors': errors}, status=400)
        user = User.objects.create(username=username, email=email, password=password)

        messages.success(request, 'Account created successfully. Please login.')
        return redirect('signin')

    return render(request, 'signup.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            login(request, user)
            return redirect('list_users')              
        else:
            return render(request, 'users.html', {'error_message': 'Invalid username or password'})

    return render(request, 'signin.html')

@login_required(login_url="/signin")'''

def list_users(request, pk_test):
    student = Student.objects.get(id=pk_test)

    return render(request, 'users.html', {'student': student})

@login_required(login_url="/signin")
def edit(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users')
        
    context = {'form':form}
    return render(request, 'student_form.html', context)
def student(request):
    return render(request,'student.html')


def signout(request):
    if request.method == 'POST':
        logout(request)
        
        return redirect('signin')  

