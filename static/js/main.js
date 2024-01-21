var categoriesOptions = ['Household', 'Food', 'Transport', 'Social Life', 'Clothes', 'Health', 'Phone', 'Education', 'Finance', 'Gift' ]

function addExpenseInput() {
    var expenseInputs = document.getElementById('expenseInputs');
    var newInput = document.createElement('div');
    newInput.className = 'expense-input';
    newInput.innerHTML = `
        <label>Category:</label>
        <select name="categories" id="categories" class="expenseCategory">
            <option value="household">Household</option>
            <option value="food">Food</option>
            <option value="transport">Transport</option>
            <option value="social_life">Social Life</option>
            <option value="clothes">Clothes</option>
            <option value="health">Health</option>
            <option value="phone_service">Phone</option>
            <option value="education">Education</option>
            <option value="finance">Finance</option>
            <option value="gift">Gift</option>
        </select>
        <label>Amount:</label>
        <input type="number" class="expenseAmount" placeholder="Enter amount" name="expense_amount" value="0" 
            min="0" max="100000">
        `;
    expenseInputs.appendChild(newInput);
}

function calculateBudget() {
    var totalBudget = document.getElementById('totalBudget').value;
    var expenseCategories = document.getElementsByClassName('expenseCategory');
    var expenseAmounts = document.getElementsByClassName('expenseAmount');
    var totalExpenses = 0;

    for (var i = 0; i < expenseAmounts.length; i++) {
        totalExpenses += parseFloat(expenseAmounts[i].value) || 0;
    }

    var remainingBudget = totalBudget - totalExpenses;

    document.getElementById('totalExpenses').innerText = 'Total Expenses: ' + totalExpenses;
    document.getElementById('remainingBudget').innerText = 'Remaining Budget: ' + remainingBudget;
}
