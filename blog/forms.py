"""
Module for defining forms related to comments.
"""

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for adding a comment.
    """
    class Meta:
        """
        Meta class specifying the model and fields for the form.
        """
        model = Comment
        fields = ('body',)
