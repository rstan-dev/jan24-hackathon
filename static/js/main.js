function addExpenseInput() {
    var expenseInputs = document.getElementById('expenseInputs');
    var newInput = document.createElement('div');
    newInput.className = 'expense-input';
    newInput.innerHTML = `
        <label>Category:</label>
        <input type="text" class="expenseCategory" placeholder="Enter category">
        <label>Amount:</label>
        <input type="number" class="expenseAmount" placeholder="Enter amount">
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