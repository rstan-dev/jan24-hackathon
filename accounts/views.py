from django.shortcuts import render

from .models import Category

# Create your views here.

def account(request):
    """ A view to show the profile of a user """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'accounts/profile.html', context)



def expenses(request):
    # Assume you have logic to calculate total_expenses for each category
    # and pass it to the template context
    categories = Category.objects.all()
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        total_expenses = calculate_total_expense(request.POST, category_name)
    else:
        total_expenses = None

    context = {
        'categories': categories,
        'total_expenses': total_expenses,
    }

    return render(request, 'accounts/expense.html', context)

def savings(request):
    # Assume you have logic to calculate total_expenses for each category
    # and pass it to the template context
    categories = Category.objects.all()
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        total_saving = calculate_total_saving(request.POST, category_name)
    else:
        total_saving = None

    context = {
        'categories': categories,
        'total_saving': total_saving,
    }

    return render(request, 'accounts/saving.html', context)

def calculate_total_expense(post_data, category_name):
    total_expense = 0

    for key, value in post_data.items():
        if key.startswith(f'expenseAmount_{category_name}_'):
            try:
                total_expense += float(value)
            except ValueError:
                pass  # Ignore invalid values

    return total_expense

def calculate_total_saving(post_data, category_name):
    total_saving = 0

    for key, value in post_data.items():
        if key.startswith(f'savingAmount_{category_name}_'):
            try:
                total_expenses = calculate_total_expense(category_name)
                total_saving = total_expenses - budget
            except ValueError:
                pass  # Ignore invalid values

    return total_saving
    