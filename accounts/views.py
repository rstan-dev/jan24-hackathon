from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index profile page """

    return render(request, 'accounts/profile.html')