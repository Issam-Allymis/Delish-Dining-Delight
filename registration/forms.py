from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', 'style': 'margin-bottom: 20px;'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'style': 'margin-bottom: 20px;'}))
    password1 = forms.CharField(label="Password", max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'style': 'margin-bottom: 20px;'}))
    password2 = forms.CharField(label="Confirm Password", max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control', 'style': 'margin-bottom: 20px;'}))

    class Meta:

        model = User 
        fields = ['username', 'email', 'password1', 'password2']










