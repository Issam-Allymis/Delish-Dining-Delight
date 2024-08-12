"""
Module containing models for the registration folder.
"""

from django.db import models

# Create your models here.

class Registration(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=40)
    date_registered = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}, Registered on: {self.date_registered.strftime('%Y-%m-%d')}"
    
    