"""On_Demand_Service URL Configuration

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

import home.views
from home import views
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('home/', home.views.home_view,name='home'),
    path('admin/', admin.site.urls),
    path('',auth_views.LoginView.as_view( template_name = 'Login_Page.html' ) ),
    # path('signup/', home.views.signup_view),
    path('about/', home.views.aboutus),
    path('categorise/', home.views.categorise),
    path('categorise/car-wash', home.views.categorise_carwash),
    path('categorise/interior', home.views.categorise_interior),
    path('categorise/computer', home.views.categorise_computer),
    path('categorise/cleaning', home.views.categorise_cleaning),
    path('categorise/homeMaid', home.views.categorise_homemaid),
    path('categorise/driving', home.views.driving_view),
    path('home/assets/css/style.css', home.views.home_view),
    path('register/',home.views.register,name='test'),
]
