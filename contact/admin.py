from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contact model.
    """
    list_display = ('name', 'email', 'date_submitted')  # Columns to display in the admin list view
    search_fields = ('name', 'email')  
    list_filter = ('date_submitted',)  
    ordering = ('-date_submitted',)  # Order by date submitted, newest first
