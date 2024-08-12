"""
Module containing views for user registration and authentication.
"""

from django.shortcuts import render, redirect

# Imported decorator to protect our view
from django.contrib.auth.decorators import login_required

# - Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm, SigninForm

def register(request):
    """
    View function for user registration.
    """
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    else:
        form = CreateUserForm()
    
    context = {'registerform': form}
    return render(request, 'registration/register.html', context)

def my_login(request):
    """
    View function for user login.
    """
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) # auth.
                return redirect('home')
    else:
        form = SigninForm()
    
    context = {'loginform': form}
    return render(request, 'registration/my_login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='my-login')
def dashboard(request):
    """
    View function for user dashboard.
    """
    return render(request, 'base.html')
