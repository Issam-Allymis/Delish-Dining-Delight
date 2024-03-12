from django.shortcuts import render, redirect
from . forms import CreateUserForm


def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("account_login")

    
    context = {'registerform': form}


    return render(request, 'registration/register.html', context)










def my_login(request):

    return render(request, 'registration/my_login.html')

