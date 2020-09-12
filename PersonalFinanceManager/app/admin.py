from django.contrib import admin
from .models import *
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'account_type', 'currency', "balance"]


admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(Account, AccountAdmin)