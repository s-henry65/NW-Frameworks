from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from nw_users_app.models import UserProfile
from nw_users_app.models import User
from nw_orders_app.models import FrameProfile
from nw_orders_app.models import Finish
from nw_orders_app.models import Wood
from nw_orders_app.models import PriceKey
from fractions import Fraction

@login_required
def place_order(request):
    current_user = request.user
    profile_data = FrameProfile.objects.all()
    finish_data = Finish.objects.all()
    wood_data = Wood.objects.all()
    if request.method == 'GET':
        context = {
            'current_user': current_user, 'profile_data': profile_data, 'finish_data': finish_data,
            'wood_data': wood_data,
        }
        return render(request, 'order/place_order.html', context)
    elif request.method == 'POST':
        # try:
            price_key = PriceKey.objects.all()
            profile = FrameProfile.objects.get(id=request.POST['profile'])
            depth = int(request.POST['depth'])
            wood = Wood.objects.get(id=request.POST['wood'])
            finish = Finish.objects.get(id=request.POST['finish'])
            key = float(profile.category.width_price)
            width = float(profile.width_quarters)
            frame_width = (request.POST['frame_width'])
            frame_height = (request.POST['frame_height'])
            # calculate profile cost
            price_profile = round((width * key) * depth, 2)
            price_wood = round(price_profile * float(wood.price_modifier), 2)
            price_finish = round(price_wood * float(finish.price_modifier), 2)
            print('Base price: ', price_profile)
            print('Price w/wood: ', price_wood)
            print('Price w/stain: ', price_finish)
            # convert fractions to float
            width_list = frame_width.split()
            height_list = frame_height.split()
            width_fraction = 0
            height_fraction = 0
            for num in width_list:
                 x=Fraction(num)
                 x=float(x)
                 width_fraction += x
            for num in height_list:
                 x=Fraction(num)
                 x=float(x)
                 height_fraction += x
            # calculate united inches
            frame_perimeter = (width_fraction + height_fraction) * 2
            print('Perimeter: ', frame_perimeter)
            united_inches = ((width / 4) * 12) + frame_perimeter
            print('Width: ', (width / 4))
            united_inches = round(united_inches / 12, 2)
            print('Frame: ', width_fraction, 'x', height_fraction)
            print('United inches: ', united_inches)
            frame_price = united_inches * price_finish
            print('Frame price: ', frame_price)
            
            # print('profile: ', profile.category)
            # print('depth: ', depth)
            # print('wood: ', wood)
            # print('finish: ', finish)
            return redirect('place_order')
        # except:
        #     context = {
        #     'current_user': current_user, 'profile_data': profile_data, 'finish_data': finish_data,
        #     'wood_data': wood_data,
        # }
        #     messages.warning(request, 'Please complete form!')
        #     return render(request, 'order/place_order.html', context)

@login_required
def order_archive(request):
    return render(request, 'order/order_archive.html')

@login_required
def frame_profiles(request):
    return render(request, 'order/frame_profiles.html')