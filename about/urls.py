"""
Module containing URL patterns for the about page functionality.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.AboutPage.as_view(), name='about'),
]
