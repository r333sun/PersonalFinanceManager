import django.utils.timezone as timezone
from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=100, decimal_places=2)


class Expense(models.Model):
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField(default=timezone.now)
    category = models.ForeignKey(to="Category", to_field="id", on_delete=models.CASCADE)
    account = models.ForeignKey(to="Account", to_field="id", on_delete=models.CASCADE)
    payee = models.CharField(max_length=100)
    note = models.TextField()


class Income(models.Model):
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField(default = timezone.now)
    account = models.ForeignKey(to="Account", to_field="id", on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    note = models.TextField()


class Budget(models.Model):
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField(default = timezone.now)
    category = models.ForeignKey(to="Category", to_field="id", on_delete=models.CASCADE)
    budget_type = models.CharField(max_length=100)
    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField(default = timezone.now)
