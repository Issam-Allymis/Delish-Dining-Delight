from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


# Register a user (Model Form)

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', 'style': 'margin-bottom: 20px;'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'style': 'margin-bottom: 20px;'}))
    password1 = forms.CharField(label="Password", max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'style': 'margin-bottom: 20px;'}))
    password2 = forms.CharField(label="Confirm Password", max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control', 'style': 'margin-bottom: 20px;'}))

    class Meta:

        model = User 
        fields = ['username', 'email', 'password1', 'password2']



# Authenticate a user (Model Form)

class SigninForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username', 'style': 'margin-bottom: 10px;'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password', 'style': 'margin-bottom: 10px;'}))


