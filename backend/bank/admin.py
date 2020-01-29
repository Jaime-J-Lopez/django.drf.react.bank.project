from django.contrib import admin
from .models import Bank, Account

# class BankAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'completed')

# Register your models here.
admin.site.register((Bank, Account))