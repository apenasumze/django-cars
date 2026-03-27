from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest


def login_view(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
        
    return render(request, 'login.html', context={'form': login_form})

def logout_view(request: HttpRequest):
    logout(request)
    return redirect('cars_list')

def register_view(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
        
    else:
        user_form = UserCreationForm()
        
    return render(request, 'register.html', context={'user_form': user_form})
