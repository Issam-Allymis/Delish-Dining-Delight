"""
Module containing URL patterns for the contact application.
"""

from django.urls import path
from . import views
from .views import contact_success

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('contact-success/', contact_success, name='contact_success'),
]
