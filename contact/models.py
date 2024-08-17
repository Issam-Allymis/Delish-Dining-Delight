"""
Module containing models for the contact application.
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

    def __str__(self):
        """
        Return a string representation of the contact.
        """
        return self.name
