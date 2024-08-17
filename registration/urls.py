"""
Module defining URL patterns for registration app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login")
]
