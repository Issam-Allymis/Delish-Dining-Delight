"""
Module containing views for the contact form functionality.
"""

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import generic, View
from django.template.loader import render_to_string 
from django.http import HttpResponseServerError
from django.contrib import messages
from .forms import ContactForm
from decouple import config
from dotenv import load_dotenv
load_dotenv()


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            content = form.cleaned_data['content']
            
            subject = f"Contact Form Submission from {name}"
            message = f"Message from: {name}\nEmail: {email}\nAddress: {address}\n\nContent:\n{content}"
            from_email = email
            recipient_list = [config('EMAIL_HOST_USER')] 
            try:
                send_mail(subject, message, from_email, recipient_list) 
                messages.success(request, 'Your message has been sent.')
                return redirect('contact')
            
            except Exception as e:
                import traceback
                error_message = traceback.format_exc()
                messages.error(request, f'Error sending email: {e}')
                print(error_message)  # or use logging
                return redirect('contact')
        else:
            print(form.errors)  # Print form errors for debugging
            messages.error(request, 'Form submission is invalid.')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    """
    Display the success page with thank you message and order content
    """
    return render(
        request,
        'contact_success.html',
    )

