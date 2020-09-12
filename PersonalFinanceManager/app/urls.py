
from django.urls import path

from . import views

urlpatterns = [
    path('list_account/', views.list_account, name="list_account"),
    path('create_account/', views.create_account, name="create_account"),
    path('delete_account/<int:account_id>/', views.delete_account, name='delete_account'),
    path('update_account/<int:account_id>/', views.update_account, name='update_account'),
    path('get_account/<int:account_id>/', views.get_account, name='get_account'),

    path('list_category/', views.list_category, name="list_category"),
    path('create_category/', views.create_category, name="create_category"),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('update_category/<int:category_id>/', views.update_category, name='update_category'),
    path('get_category/<int:category_id>/', views.get_category, name='get_category'),

    path('list_expense/', views.list_expense, name="list_expense"),
    path('create_expense/', views.create_expense, name="create_expense"),
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('update_expense/<int:expense_id>/', views.update_expense, name='update_expense'),
    path('get_expense/<int:expense_id>/', views.get_expense, name='get_expense'),

    path('list_income/', views.list_income, name="list_income"),
    path('create_income/', views.create_income, name="create_income"),
    path('delete_income/<int:income_id>/', views.delete_income, name='delete_income'),
    path('update_income/<int:income_id>/', views.update_income, name='update_income'),
    path('get_income/<int:income_id>/', views.get_income, name='get_income'),

    path('list_budget/', views.list_budget, name="list_budget"),
    path('create_budget/', views.create_budget, name="create_budget"),
    path('delete_budget/<int:budget_id>/', views.delete_budget, name='delete_budget'),
    path('update_budget/<int:budget_id>/', views.update_budget, name='update_budget'),
    path('get_budget/<int:budget_id>/', views.get_budget, name='get_budget'),
]