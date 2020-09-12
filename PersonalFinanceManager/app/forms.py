from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = "__all__"
