from django.contrib import admin
from django.urls import path
from . import views
from .views import about_us

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us.html/', about_us, name='about_us'),
]