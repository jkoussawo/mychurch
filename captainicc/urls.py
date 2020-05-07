from django.contrib import admin
from django.urls import path
from captainicc import views

urlpatterns = [
    path('',views.membre_list, name ='membres-list' ),
    path('membres/',views.membre_list, name ='membres-list' ),
    path('membres/add_membre',views.add_membre, name ='add-membre' ),
    path('membres/profile',views.list_membre_profile, name ='profile-membre' ),
    path('membres/welcome',views.welcome, name ='welcome' ),
]
