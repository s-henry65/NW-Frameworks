from django.urls import path
from . import views

urlpatterns = [
    path('sign_in/', views.sign_in, name = 'sign_in'),
    path('', views.index, name = 'index'),
    path('login_user/', views.login_user, name = 'login_user'),
    path('client_index/', views.client_index, name = 'client_index'),
    path('logout_user/', views.logout_user, name = 'logout_user'),
    path('create_user/', views.create_user, name = 'create_user'),
    path('update_user_profile/', views.update_user_profile, name = 'update_user_profile'),
    path('create_user_profile/<int:id>', views.create_user_profile, name = 'create_user_profile'),
    path('site_admin/', views.site_admin, name = 'site_admin'),
    path('active_orders/', views.active_orders, name = 'active_orders'),
    path('update_order/<int:id>', views.update_order, name = 'update_order'),
    path('admin_order_archive/', views.admin_order_archive, name = 'admin_order_archive'),
]