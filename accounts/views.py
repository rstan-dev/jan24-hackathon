from django.shortcuts import render, redirect
from .models import Category
from .forms import MyForm

# Create your views here.

def account(request):
    """ A view to show the profile of a user """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'accounts/profile.html', context)

def update_budget(request):
    """  """

    categories = Category.objects.all()

    total_budget = int(request.POST.get('total_budget'))
    redirect_url = request.POST.get('redirect_url')
    amount = int(request.POST.get('expense_amount'))
    
    expenses = request.session.get('expenses', {})

    category_name = str(request.POST.get('categories'))
    
    # for category in categories:
    if category_name in list(expenses.keys()):
        expenses[category_name] += amount
    else:
        expenses[category_name] = amount

    request.session['expenses'] = expenses
    print(request.session['expenses'])
    print(total_budget)

    return redirect(redirect_url)
