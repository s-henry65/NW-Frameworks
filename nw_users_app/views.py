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
from nw_users_app.models import User

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
    try:
        current_user = request.user
        id = current_user.id
        user_data = UserProfile.objects.get(user_name = current_user)
        context = { 'user_data' : user_data
        }
        return render(request, 'user/client_index.html', context)
    except:
        messages.warning(request, 'Please setup a User Profile to continue')
        return redirect('create_user_profile', id)
    

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

@login_required
def create_user_profile(request, id):
    current_user = request.user
    # id = current_user.id
    user_data = User.objects.get(id=id)
    context = { 'user_data' : user_data
    }
    if request.method == 'GET':
        return render(request, 'user/user_profile.html', context)
    elif request.method == 'POST':
        user_name = current_user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_num = request.POST['phone_num']
        email = request.POST['email']
        shop_name = request.POST['shop_name']
        shop_address = request.POST['shop_address']
        shop_city = request.POST['shop_city']
        shop_state = request.POST['shop_state']
        shop_zipcode = request.POST['shop_zipcode']
        
        UserProfile.objects.create(first_name = first_name, last_name = last_name, phone_num = phone_num, 
                                    email = email, shop_name = shop_name, shop_address = shop_address,
                                    shop_city = shop_city, shop_state = shop_state, shop_zipcode = shop_zipcode, 
                                    user_name = user_name)
        return redirect('client_index')
    
@login_required
def update_user_profile(request):
    current_user = request.user
    user_data = UserProfile.objects.get(user_name = current_user)
    print('USER: ', user_data)
    context = { 'user_data' : user_data
    }
    if request.method == 'GET':
        return render(request, 'user/update_user_profile.html', context)
    elif request.method == 'POST':
        user_data.first_name = request.POST['first_name']
        user_data.last_name = request.POST['last_name']
        user_data.phone_num = request.POST['phone_num']
        user_data.email = request.POST['email']
        user_data.shop_name = request.POST['shop_name']
        user_data.shop_address = request.POST['shop_address']
        user_data.shop_city = request.POST['shop_city']
        user_data.shop_state = request.POST['shop_state']
        user_data.shop_zipcode = request.POST['shop_zipcode']
        user_data.save()
        messages.warning(request, 'User profile updated!')
        return redirect('client_index')