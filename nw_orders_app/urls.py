from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name = 'place_order'),
    path('order_archive/', views.order_archive, name = 'order_archive'),
    path('frame_profiles/', views.frame_profiles, name = 'frame_profiles'),
    path('cart/', views.cart, name = 'cart'),
    path('close_cart/<int:id>', views.close_cart, name = 'close_cart'),
]