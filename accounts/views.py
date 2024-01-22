from django.shortcuts import render, redirect, get_object_or_404, reverse
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

    if category_name in list(expenses.keys()):
        expenses[category_name] += amount
    else:
        expenses[category_name] = amount

    request.session['expenses'] = expenses
    request.session['total_budget'] = total_budget

    return redirect(redirect_url)


def adjust_budget(request):
    """ """

    category = str(request.POST.get('used_category'))
    new_amount = int(request.POST.get('new_amount'))
    redirect_url = request.POST.get('redirect_url')

    expenses = request.session.get('expenses', {})

    if new_amount > 0:
        expenses[category] = new_amount
    else:
        expenses.pop(category)

    # overwrite the variable with the updated version
    request.session['expenses'] = expenses

    return redirect(reverse('profile'))


def expense_planner_function(request):
    """ """
    
    categories = Category.objects.all()

    expenses = request.session.get('expenses', {})
    redirect_url = request.POST.get('redirect_url')
    
    left_amounts = request.session.get('left_amounts', {})
    expense_planner_amounts = request.session.get('expense_planner_amounts', {})

    for category, amount in expenses.items():
        expense_planner_amount = int(request.POST.get(f'expense_planner_amount_{category}', 0))
        left_amount = expense_planner_amount - amount
        left_amounts[category] = left_amount
        expense_planner_amounts[category] = expense_planner_amount
    
    # overwrite the variables with the updated version
    request.session['left_amounts'] = left_amounts
    request.session['expense_planner_amounts'] = expense_planner_amounts
    # request.session['expense_planner_amount'] = expense_planner_amount

    total_left = sum(left_amounts.values())

    context = {
        'expense_planner_amount_category': expense_planner_amount,
        'amount': amount,
        'left_amount': left_amount,
        'left_amounts': left_amounts,
        'category': category,
        'expense_planner_amounts': expense_planner_amounts,
        'total_left': total_left,
    }

    return render(request, 'accounts/expense.html', context)


# Bekry:
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

# Sam's Page:
def about(request):
    """ A view to show the about us page """

    return render(request, 'accounts/about.html')

