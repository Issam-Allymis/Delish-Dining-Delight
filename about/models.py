"""
Module containing models for the about page functionality.
"""

from django.db import models
from django.utils import timezone

class About(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the About page")
    mission_statement = models.TextField(help_text="Mission statement of the company")
    history = models.TextField(help_text="Brief history of the company", null=True, blank=True)
    values = models.TextField(help_text="Core values of the company", null=True, blank=True)
    milestones = models.TextField(help_text="Key milestones in the company's history", null=True, blank=True)
    image = models.ImageField(upload_to='about_images/', null=True, blank=True, help_text="Optional image for the About page")
    published_date = models.DateTimeField(default=timezone.now, help_text="Date the About page was published")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"