# from django.contrib import admin
from django.urls import path,include
from . import views

app_name='Dishes'

urlpatterns = [
  
    path('', views.Restaurant_list,name='Restaurant_list'),
    path('Restaurant/<str:slug>/', views.Restaurant_items, name ="Restaurant_items"),
]

