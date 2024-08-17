"""
Module containing admin configurations for the about page functionality.
"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model.
    """
    list_display = ('title', 'published_date')
    search_fields = ('title', 'mission_statement', 'history', 'values')
    summernote_fields = ('mission_statement', 'history', 'values', 'milestones')
