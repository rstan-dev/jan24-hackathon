# Context processor which makes all the variables available 


def budget_content(request):

    expenses = []
    total_budget = 0

    context = {
        'expenses': expenses,
        'total_budget': total_budget,
    }

    return context
