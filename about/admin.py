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
    list_display = ('title',)
    search_fields = (['title', 'content'])
    summernote_fields = ('content',)
