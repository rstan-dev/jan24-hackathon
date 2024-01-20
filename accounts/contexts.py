# Context processor which makes all the variables available 
from . import models
from django.conf import settings


def budget_content(request):

    total_budget = int(request.session.get('total_budget'))
    total_expenses = 0
    expenses = request.session.get('expenses', {})
    
    for category_name, amount in expenses.items():
        total_expenses += amount

    total = total_budget - total_expenses

    context = {
        'expenses': expenses,
        'total_budget': total_budget,
        'total_expenses': total_expenses,
        'total': total,
    }

    return context
