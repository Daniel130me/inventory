"""myinventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard import views as dashboard_views
from user import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_views.index, name='dashboard-index' ),
    path('staff/', dashboard_views.staff, name='dashboard-staff' ),
    path('product/', dashboard_views.product, name='dashboard-product'),
    path('product_details/', dashboard_views.product_details, name='user-product-details'),
    path('product_update/', dashboard_views.product_update, name='user-product-update'),
    path('product/<int:id>', dashboard_views.product_delete, name='user-product-delete'),
    path('order/', dashboard_views.order, name='dashboard-order' ),
    path('staff_order_details/', dashboard_views.staff_order_details, name='staff_order_details'),
    path('register/', user_views.register, name='user-register' ),
    path('profile/', user_views.profile, name='user-profile' ),
    path('profile_details/', user_views.profile_details, name='user-profile-details'),
    path('login/', user_views.signin, name='user-login' ),
    path('logout/', user_views.signout, name='user-logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login' ),
    # path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
]
