"""
Module containing models for the about page functionality.
"""

from django.db import models

class About(models.Model):
    """
    Model representing information about the website.
    """
    title = models.CharField(max_length=80, unique=True)
    content = models.TextField()

    def __str__(self):
        """
        Return a string representation of the title.
        """
        return self.title
