"""
Module containing URL patterns for the contact application.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Contact.as_view(), name='contact'),
    path('success/', views.contact_success, name='contact_success'),
]
