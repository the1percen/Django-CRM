from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome to Django CRM")
            return redirect('index')
        else:
            messages.error(request, "Bad Credentials")
            return redirect('index')
    context = {}
    return render(request, "index.html", context=context)

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Your Successfully logged out")
    return redirect('index')

def register(request):
    context = {}
    return render(request, "register.html", context=context)