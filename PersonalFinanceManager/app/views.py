from django.shortcuts import render, redirect
from .forms import *


def list_account(request):
    accounts = Account.objects.all()

    return render(request, 'list_account.html', {"accounts": accounts})


def create_account(request):
    if request.method == 'POST':
        account = AccountForm(request.POST)

        if account.is_valid():
            account.save()
            return redirect('list_account')

    form = AccountForm()
    return render(request, 'create_account.html', {'form': form})


def delete_account(request, account_id):
    account = Account.objects.get(id=account_id)

    if request.method == 'POST':
        account.delete()
        return redirect('list_account')

    return render(request, 'delete_account.html', {'account': account})


def update_account(request, account_id):
    account = Account.objects.get(id=account_id)

    if request.method == 'POST':
        account = AccountForm(instance=account, data=request.POST)

        if account.is_valid():
            account.save()
            return redirect('list_account')

    form = AccountForm(instance=account)
    return render(request, 'update_account.html', {'form': form, 'account': account})


def get_account(request, account_id):
    account = Account.objects.get(id=account_id)

    if request.method == 'POST':
        return redirect('list_account')

    return render(request, 'get_account.html', {'account': account})


def list_category(request):
    categorys = Category.objects.all()

    return render(request, 'list_category.html', {"categorys": categorys})


def create_category(request):
    if request.method == 'POST':
        category = CategoryForm(request.POST)

        if category.is_valid():
            category.save()
            return redirect('list_category')

    form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)

    if request.method == 'POST':
        category.delete()
        return redirect('list_category')

    return render(request, 'delete_category.html', {'category': category})


def update_category(request, category_id):
    category = Category.objects.get(id=category_id)

    if request.method == 'POST':
        category = CategoryForm(instance=category, data=request.POST)

        if category.is_valid():
            category.save()
            return redirect('list_category')

    form = CategoryForm(instance=category)
    return render(request, 'update_category.html', {'form': form, 'category': category})


def get_category(request, category_id):
    category = Category.objects.get(id=category_id)

    if request.method == 'POST':
        return redirect('list_category')

    return render(request, 'get_category.html', {'category': category})


def list_expense(request):
    expenses = Expense.objects.all()

    return render(request, 'list_expense.html', {"expenses": expenses})


def create_expense(request):
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)

        if expense.is_valid():
            account = expense.cleaned_data['account']
            date = expense.cleaned_data['date']
            existed_budget = Budget.objects.filter(category=expense.cleaned_data['category'], start_date__lte=date,
                                        end_date__gte=date)

            if existed_budget:
                budget = existed_budget.first()
                account.balance -= expense.cleaned_data['amount']
                budget.amount -= expense.cleaned_data['amount']

                budget.save()
                account.save()
                expense.save()
                return redirect('list_expense')

    form = ExpenseForm()
    return render(request, 'create_expense.html', {'form': form})


def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        account = expense.account
        date = expense.date
        existed_budget = Budget.objects.filter(category=expense.category, start_date__lte=date,
                                    end_date__gte=date)
        if existed_budget:
            budget = existed_budget.first()
            account.balance += expense.amount
            budget.amount += expense.amount

            budget.save()
            account.save()
            expense.delete()
            return redirect('list_expense')

    return render(request, 'delete_expense.html', {'expense': expense})


def update_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)

    if request.method == 'POST':
        old_amount = expense.amount
        expense = ExpenseForm(instance=expense, data=request.POST)

        if expense.is_valid():
            account = expense.cleaned_data['account']
            date = expense.cleaned_data['date']
            existed_budget = Budget.objects.filter(category=expense.cleaned_data['category'], start_date__lte=date,
                                        end_date__gte=date)

            if existed_budget:
                budget = existed_budget.first()
                account.balance -= expense.cleaned_data['amount'] - old_amount
                budget.amount -= expense.cleaned_data['amount'] - old_amount

                budget.save()
                account.save()
                expense.save()
                return redirect('list_expense')

    form = ExpenseForm()
    return render(request, 'update_expense.html', {'form': form, 'expense': expense})


def get_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)

    if request.method == 'POST':
        return redirect('list_expense')

    return render(request, 'get_expense.html', {'expense': expense})


def list_income(request):
    incomes = Income.objects.all()

    return render(request, 'list_income.html', {"incomes": incomes})


def create_income(request):
    if request.method != 'POST':
        income = IncomeForm(request.POST)

        if income.is_valid():
            account = income.cleaned_data['account']
            account.balance += income.cleaned_data['amount']

            account.save()
            income.save()
            return redirect('list_income')

    form = IncomeForm()
    return render(request, 'create_income.html', {'form': form})


def delete_income(request, income_id):
    income = Income.objects.get(id=income_id)

    if request.method == 'POST':
        account = income.account
        account.balance -= income.amount

        account.save()
        income.delete()
        return redirect('list_income')

    return render(request, 'delete_income.html', {'income': income})


def update_income(request, income_id):
    income = Income.objects.get(id=income_id)

    if request.method == 'POST':
        old_amount = income.amount
        income = IncomeForm(instance=income, data=request.POST)

        if income.is_valid():
            account = income.cleaned_data['account']
            account.balance += income.cleaned_data['amount'] - old_amount

            account.save()
            income.save()
            return redirect('list_income')

    form = IncomeForm(instance=income)
    return render(request, 'update_income.html', {'form': form, 'income': income})


def get_income(request, income_id):
    income = Income.objects.get(id=income_id)

    if request.method == 'POST':
        return redirect('list_income')

    return render(request, 'get_income.html', {'income': income})


def list_budget(request):
    budgets = Budget.objects.all()

    return render(request, 'list_budget.html', {"budgets": budgets})


def create_budget(request):
    if request.method == 'POST':
        budget = BudgetForm(request.POST)

        if budget.is_valid():
            existed_budget = Budget.objects.filter(category=budget.cleaned_data['category'],
                                                   end_date__gte=budget.cleaned_data['start_date'])

            if not existed_budget:
                budget.save()
                return redirect('list_budget')

    form = BudgetForm()
    return render(request, 'create_budget.html', {'form': form})


def delete_budget(request, budget_id):
    budget = Budget.objects.get(id=budget_id)

    if request.method == 'POST':
        budget.delete()
        return redirect('list_budget')

    return render(request, 'delete_budget.html', {'budget': budget})


def update_budget(request, budget_id):
    budget = Budget.objects.get(id=budget_id)

    if request.method == 'POST':
        budget = BudgetForm(instance=budget, data=request.POST)

        if budget.is_valid():
            existed_budget = Budget.objects.filter(category=budget.cleaned_data['category'],
                                                   end_date__gte=budget.cleaned_data['start_date']).exclude(
                id=budget_id)

            if not existed_budget:
                budget.save()
                return redirect('list_budget')

    form = BudgetForm(instance=budget)
    return render(request, 'update_budget.html', {'form': form, 'budget': budget})


def get_budget(request, budget_id):
    budget = Budget.objects.get(id=budget_id)

    if request.method == 'POST':
        return redirect('list_budget')

    return render(request, 'get_budget.html', {'budget': budget})
