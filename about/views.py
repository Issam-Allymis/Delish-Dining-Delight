from django.shortcuts import render
from django.views import generic, View
from .models import About


class About(View):
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
