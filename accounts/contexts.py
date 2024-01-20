# Context processor which makes all the variables available 


def budget_content(request):

    total_budget = 0
    total_expenses = 0
    expenses = request.session.get('expenses', {})
    
    for category_name, amount in expenses.items():
        total_expenses += amount

    context = {
        'expenses': expenses,
        'total_budget': total_budget,
        'total_expenses': total_expenses
    }

    return context
