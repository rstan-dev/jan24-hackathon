from django.shortcuts import render
from . import templates
# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'account/login.html')
