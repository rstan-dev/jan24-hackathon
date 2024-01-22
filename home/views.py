from django.shortcuts import render
# from . import templates
# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'account/login.html')

def about_us(request):
    """ A view to return the about page """
    
    return render(request, 'home/about-us.html') 
