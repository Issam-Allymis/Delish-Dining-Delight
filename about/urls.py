"""
Module containing URL patterns for the about page functionality.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.AboutPage, name='about'), # .as_view()
]
