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
from nw_orders_app.models import Spline
from nw_orders_app.models import Corner
from nw_orders_app.models import Gold
from nw_orders_app.models import Bole
from nw_orders_app.models import TopTreatment
from nw_orders_app.models import SideTreatment
from nw_orders_app.models import Order
from nw_orders_app.models import OrderItem
from fractions import Fraction
from datetime import date

@login_required
def place_order(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_name=current_user)
    profile_data = FrameProfile.objects.all()
    finish_data = Finish.objects.all()
    wood_data = Wood.objects.all()
    spline_data = Spline.objects.all()
    gold_data = Gold.objects.all()
    bole_data = Bole.objects.all()
    side_data = SideTreatment.objects.all()
    top_data = TopTreatment.objects.all()

    
    if request.method == 'GET':
        try:
            order = Order.objects.get(customer=profile.id, complete=False)
            frame_total = order.get_cart_items
            context = {
                'current_user': current_user, 'profile_data': profile_data, 'finish_data': finish_data,
                'wood_data': wood_data, 'spline_data': spline_data, 'frame_total': frame_total,
                'gold_data': gold_data, 'bole_data': bole_data, 'side_data': side_data, 'top_data': top_data,
            }
            return render(request, 'order/place_order.html', context)
        except:
            order = Order.objects.create(customer=profile, complete=False)
            context = {
                'current_user': current_user, 'profile_data': profile_data, 'finish_data': finish_data,
                'wood_data': wood_data, 'spline_data': spline_data,
                'gold_data': gold_data, 'bole_data': bole_data, 'side_data': side_data, 'top_data': top_data,
            }
            return render(request, 'order/place_order.html', context)
    elif request.method == 'POST':
        # try:
            order = Order.objects.get(customer=profile, complete=False)
            profile = FrameProfile.objects.get(id=request.POST['profile'])
            corner = Corner.objects.get(name=request.POST['radius'])
            depth = int(request.POST['depth'])
            spline = Spline.objects.get(id=request.POST['spline'])
            wood = Wood.objects.get(id=request.POST['wood'])
            finish = Finish.objects.get(id=request.POST['finish'])
            key = float(profile.category.width_price)
            width = float(profile.width_quarters)
            frame_width = (request.POST['frame_width'])
            frame_height = (request.POST['frame_height'])
            print('Corner: ',corner.price)
            quantity = (request.POST['quantity'])
            # gold data
            if request.POST.get('gold', False):
                gold_ordered = True
            else:
                gold_ordered = False
            print('Gold Status: ', gold_ordered)
            if gold_ordered == True:
                bole = Bole.objects.get(id=request.POST['bole'])
                print('Bole: ', bole.name)
                top = TopTreatment.objects.get(id=request.POST['top'])
                print('Top: ', top.name, top.gold)
                side = SideTreatment.objects.get(id=request.POST['side'])
                print('Side: ', side.name, side.gold)
        
            # calculate profile cost
            price_profile = round((width * key) * depth, 2)
            price_wood = round(price_profile * float(wood.price_modifier), 2)
            print('Base Price: ', price_wood)
            price_finish = round(price_wood * float(finish.price_modifier), 2)
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
            united_inches = ((width / 4) * 12) + frame_perimeter
            print('Width: ', (width / 4))
            united_inches = round(united_inches / 12, 2)
            print('Price w/finish: ', price_finish)
            print('United inches: ', united_inches)
            frame_price = round(united_inches * price_finish, 2)
            print('Frame price: ', frame_price)
            # add $ for radius corners
            frame_price += float(corner.price)
            print('Frame price w/corners: ', frame_price)
            if gold_ordered == True:
                OrderItem.objects.create(profile=profile, depth=depth, wood=wood, spline=spline, corner=corner,
                                                finish=finish, width=width_fraction, height=height_fraction, 
                                                ui=united_inches, price_ui=price_finish, frame_price=frame_price,
                                                quantity=quantity, gold_ordered=gold_ordered, side_treatment=side,
                                                top_treatment=top, bole=bole, order=order,)
                return redirect('cart')
            else:
                OrderItem.objects.create(profile=profile, depth=depth, wood=wood, spline=spline, corner=corner,
                                                finish=finish, width=width_fraction, height=height_fraction, 
                                                ui=united_inches, price_ui=price_finish, frame_price=frame_price,
                                                quantity=quantity, order=order,)
                return redirect('cart')
        # except:
        #     context = {
        #     'current_user': current_user, 'profile_data': profile_data, 'finish_data': finish_data,
        #     'wood_data': wood_data,
        # }
        #     messages.warning(request, 'Please complete form!')
        #     return render(request, 'order/place_order.html', context)

@login_required
def order_archive(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_name=current_user)
    context = {
        'profile': profile,
    }
    if request.method == 'GET':
        return render(request, 'order/order_archive.html', context)
    
    elif request.method == 'POST':
        current_user = request.user
        profile = UserProfile.objects.get(user_name=current_user)
        order_month = request.POST['month']
        order_year = request.POST['year']
        if order_month == 'all':
            order = Order.objects.filter(customer=profile, complete=True, order_date__year=order_year)
            context = {
            'profile': profile, 'order': order,
            }
            if order.count() == 0:
                messages.warning(
                    request, 'There are no orders for this selection.')
                return render(request, 'order/order_archive.html', context)
            else:
                return render(request, 'order/order_archive.html', context)
        else:
            order = Order.objects.filter(customer=profile, complete=True, order_date__year=order_year,
                order_date__month=order_month)
            context = {
            'profile': profile, 'order': order,
            }
            if order.count() == 0:
                messages.warning(
                    request, 'There are no orders for this selection.')
                return render(request, 'order/order_archive.html', context)
            else:
                return render(request, 'order/order_archive.html', context)

@login_required
def frame_profiles(request):
    return render(request, 'order/frame_profiles.html')

@login_required
def cart(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_name=current_user)
    try:
        order = Order.objects.get(customer=profile.id, complete=False)
        items = order.orderitem_set.all()
        frame_total = order.get_cart_items
        total_cost = order.get_cart_total
        context = {
            'order': order, 'profile': profile, 'items': items, 'frame_total': frame_total,
            'total_cost': total_cost,
        }
        return render(request, 'order/cart.html', context)
    except:
        order = Order.objects.create(customer=profile, complete=False)
        context = {
            'order': order, 'profile': profile, 
        }
        return render(request, 'order/cart.html', context)
   
@login_required
def close_cart(request, id):
    today = date.today()
    order = Order.objects.get(id=id)
    order.frame_total = order.get_cart_items
    order.total_cost = order.get_cart_total
    notes = request.POST.get('text')
    order.notes = notes
    order.complete = True
    order.order_date = today
    order.save()
    messages.warning(request, 'Order Submitted!')
    return redirect('client_index')