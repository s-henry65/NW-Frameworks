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
from nw_orders_app.models import Order
# from nw_users_app.models import Retailer

def sign_in(request):
    return render(request, 'user/login.html')

def index(request):
    return render(request, 'main-site/index.html')

def site_admin(request):
    return render(request, 'user/admin.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_staff:
            login(request, user)
            return redirect('site_admin')
        else:
            login(request, user)
            return redirect('client_index')
    else:
        messages.warning(request, 'User Name or Password is incorrect')
        return render(request, 'user/login.html')

@login_required
def client_index(request):
    current_user = request.user
    if current_user.is_staff:
        return render(request, 'user/client_index.html')
    try:
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
        return render(request, 'user/create_user_profile.html', context)
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
    # print('USER: ', user_data)
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
    
@login_required
def active_orders(request):
    order = Order.objects.filter(archive=False)
    context = {
        'order': order,
    }
    if order.count() == 0:
        messages.warning(
            request, 'There are no orders for this selection.')
        return render(request, 'user/active_orders.html', context)
    else:
        return render(request, 'user/active_orders.html', context)
    

@login_required
def update_order(request, id):
    if request.method == 'GET':
        order = Order.objects.get(id=id)
        # print('ORDER: ', order)
        if request.method == 'GET':
            context = {'order': order,
                    }
            return render(request, 'user/update_order.html', context)
    
    if request.method == 'POST':
        order = Order.objects.get(id=id)
        if request.POST.get('delivered', False):
            order.order_delivered = True
        if request.POST.get('paid', False):
            order.order_paid = True
        if request.POST.get('archive', False):
            order.archive = True
        order.save()
        try:
            order.due_date = request.POST['due_date']
            order.save()
        except:
            return redirect('active_orders')
    
def admin_order_archive(request):
    user_data = UserProfile.objects.all()
    context = { 'user_data': user_data,
    }
    if request.method == 'GET':
        return render(request, 'user/admin_order_archive.html', context)
    
    elif request.method == 'POST':
        customer = request.POST['shop']
        order_month = request.POST['month']
        order_year = request.POST['year']
        # print('CUSTOMER: ', customer)
        # search_results = Order.objects.filter(customer=customer, archive=True)
        if order_month == 'all':
            search_results = Order.objects.filter(customer=customer, archive=True, order_date__year=order_year)
            context = {
            'search_results': search_results, "user_data": user_data,
            }
            if search_results.count() == 0:
                messages.warning(
                    request, 'There are no orders for this selection.')
                return render(request, 'user/admin_order_archive.html', context)
            else:
                return render(request, 'user/admin_order_archive.html', context)
        else:
            search_results = Order.objects.filter(customer=customer, archive=True, order_date__year=order_year,
                order_date__month=order_month)
            context = {
            'search_results': search_results, 'user_data': user_data,
            }
            if search_results.count() == 0:
                messages.warning(
                    request, 'There are no orders for this selection.')
                return render(request, 'user/admin_order_archive.html', context)
            else:
                return render(request, 'user/admin_order_archive.html', context)
    
@login_required
def update_user(request):
    shops = UserProfile.objects.all()
    context = { 'shops' : shops
    }
    return render(request, 'user/update_user.html', context)

# @login_required
# def edit_user_data(request, id):
#     if request.method == 'GET':
#         shop = Retailer.objects.get(id=id)
#         context = {
#             'shop': shop,
#         }
#         return render(request, 'user/edit_retailer.html', context)
#     elif request.method == 'POST':
#         shop = Retailer.objects.get(id=id)
#         shop.phone_num = request.POST['phone_num']
#         shop.website = request.POST['website']
#         shop.shop_name = request.POST['shop_name']
#         shop.shop_address = request.POST['shop_address']
#         shop.shop_city = request.POST['shop_city']
#         shop.shop_state = request.POST['shop_state']
#         shop.shop_zipcode = request.POST['shop_zipcode']
#         shop.save()
#         messages.warning(request, 'Retailer updated!')
#         return redirect('site_admin')
    

@login_required
def delete_user(request, id):
    shop = UserProfile.objects.get(id = id)
    shop.delete()
    return redirect('update_user')