from django.contrib import admin
from django.urls import path
from .views import account, expenses, savings
from .views import account, expenses

urlpatterns = [

    path('', views.account, name='profile'),
    path('update/', views.update_budget, name='update_budget'),
    path('adjust_budget/', views.adjust_budget, name='adjust_budget'),
    
    path('expense_summary/', expenses, name='expense'),
    path('saving_summary/', savings, name='saving'),

]
