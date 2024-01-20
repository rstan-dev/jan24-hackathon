from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='profile'),
    path('update/', views.update_budget, name='update_budget'),
    path('adjust_budget/', views.adjust_budget, name='adjust_budget'),
]
