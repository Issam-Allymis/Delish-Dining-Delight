from django.shortcuts import render, redirect
from . forms import CreateUserForm, SigninForm

from django.contrib.auth.decorators import login_required # Imported decorator to protect our view

# - Authentication models and functions
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login, logout


def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("my-login")

    
    context = {'registerform': form}


    return render(request, 'registration/register.html', context)




def my_login(request):
    
    form = SigninForm()

    if request.method == "POST":
        form = SigninForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('home')

    context = {'loginform': form}


    return render(request, 'registration/my_login.html', context)



@login_required(login_url='my-login')
def dashboard(request):

    return render(request, 'base.html')

