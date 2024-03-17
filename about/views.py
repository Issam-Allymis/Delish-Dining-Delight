"""
Module containing views for the about page functionality.
"""

from django.shortcuts import render
from django.views import View


class AboutPage(View):
    """
    Class based View to render About Page
    """

    def get(self, request, *args, **kwargs):
        """
        Renders about page
        """

        return render(
            request,
            "about.html",
        )
