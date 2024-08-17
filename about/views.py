"""
Module containing views for the about page functionality.
"""

from django.shortcuts import render
from .models import About

def AboutPage(request):
    about_content = About.objects.first()  # Assuming there's only one about page entry
    return render(request, 'about.html', {'about': about_content})
