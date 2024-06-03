from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserInfo
#from .forms import UserForm


User = get_user_model()

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
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

        user = UserInfo.objects.create(firstname= firstname,lastname=lastname, email=email, phone= phone)

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

@login_required(login_url="/signin")
def list_users(request):
    users = UserInfo.objects.all()
    return render(request, 'users.html', {'users': users})

@login_required(login_url="/signin")
def edit(request):
    return render(request, ('edit.html'))
def student(request):
    return render(request,'student.html')


def signout(request):
    if request.method == 'POST':
        logout(request)
        
        return redirect('signin')  

