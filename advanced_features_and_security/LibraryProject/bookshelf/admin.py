from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Extra info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Extra info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

admin.site.register(CustomUser, CustomUserAdmin)
