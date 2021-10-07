from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ['email', 'username', 'department', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin','is_staff']
    search_fields = ['email', 'username', 'department', 'first_name', 'last_name']
    readonly_fields = ['date_joined', 'last_login']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('department', 'first_name', 'last_name')}),
    )
admin.site.register(Account, AccountAdmin)


