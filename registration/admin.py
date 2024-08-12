from django.contrib import admin
from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Registration model.
    """
    list_display = ('username', 'email', 'date_registered')  # Columns to display in the admin list view
    search_fields = ('username', 'email')  # Fields to include in the admin search bar
    list_filter = ('date_registered',)  # Add a filter sidebar to filter by date registered
    ordering = ('-date_registered',)  # Order by date registered, newest first
