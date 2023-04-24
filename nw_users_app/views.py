import os
from django.shortcuts import render, redirect
# import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from nw_users_app.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def sign_in(request):
    return render(request, 'user/login.html')

def index(request):
    return render(request, 'main-site/index.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('client_index')
    else:
        messages.warning(request, 'User Name or Password is incorrect')
        return render(request, 'user/login.html')

@login_required
def client_index(request):
    return render(request, 'user/client_index.html')

def logout_user(request):
    logout(request)
    return redirect('index')

@login_required
def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request, 'New user successfully added!')
            return redirect(create_user) 
        else:
            return render(request, "user/create_user.html", {'form': form}) 
    else:
        form = CreateUserForm()
        context = {
            'form': form,
        }
        return render(request, 'user/create_user.html', context)