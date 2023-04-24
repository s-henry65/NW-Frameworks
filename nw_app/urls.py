from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('contact/', views.contact, name = 'contact'),
    path('trade/', views.trade, name = 'trade'),
    path('retailer/', views.retailer, name = 'retailer'),
    path('restoration/', views.restoration, name = 'restoration'),
    
]