"""
Module containing models for the contact folder.
"""

from django.db import models

class Contact(models.Model):
    """
    Model representing contact information.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    content = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name} on {self.date_submitted.strftime('%Y-%m-%d')}"
