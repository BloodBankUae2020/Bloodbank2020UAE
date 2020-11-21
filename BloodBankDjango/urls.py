"""BloodBankDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from bloodbank.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('login',adminlogin,name='login'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('admin_home',admin_home,name='admin_home'),
    path('logout',Logout,name='logout'),
    path('changepassword', changepassword, name='changepassword'),
    path('unread_queries', unread_queries, name='unread_queries'),
    path('read_queries', read_queries, name='read_queries'),
    path('view_queries/<int:pid>', view_queries, name="view_queries"),
    path('add_bloodgroup', add_bloodgroup, name='add_bloodgroup'),
    path('view_bloodgroup',view_bloodgroup, name='view_bloodgroup'),
    path('delete_bloodgroup(?P<int:pid>)',delete_bloodgroup,name='delete_bloodgroup'),
    path('add_donor', add_donor, name='add_donor'),
    path('becomedonor', becomedonor, name='becomedonor'),
    path('donorlist',donorlist, name='donorlist'),
    path('delete_donor(?P<int:pid>)',delete_donor,name='delete_donor'),
    path('view_donordetail/<int:pid>',view_donordetail, name="view_donordetail"),
    path('user_search', user_search, name="user_search"),
    path('booking_search', booking_search, name="booking_search"),
path('blood_search', blood_search, name="blood_search"),
    path('bookingbtwdates',bookingbtwdates, name="bookingbtwdates"),
    path('betweendate_report',betweendate_report, name="betweendate_report"),

]
