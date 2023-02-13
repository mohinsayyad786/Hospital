from django.contrib import admin
from django.urls import path
from sperohelthapp import views

urlpatterns = [
    path('hom',views.homes),
    path('',views.index),
    path('add',views.addpt),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('search',views.search),
    path('msearch',views.searchmobile),
    
    


]