from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import generic, View
from django.template.loader import render_to_string 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseServerError
from .forms import ContactForm

class contact(View):
    """
    Class based View to render contact Page
    """

    def get(self, request, *args, **kwargs):
        """
        Renders contact page
        """
        form = ContactForm() # Instantiate the ContactForm
        return render(
            request,
            "contact.html",
            {"form": form}
        )

    def post(self, request, *args, **kwargs):
        """
        Handles the form submission
        """
        form = ContactForm(request.POST)  # Bind POST data to the form
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            # Define thank you message
            thank_you_message = 'Thank you for ordering with us!, Bon appetit!'

            html_message = f"""
                <html>
                <body>
                    <p>Name: {name}</p>
                    <p>Email: {email}</p>
                    <p>Order Deatails: {content}</p>
                    <p>Message: {thank_you_message}</p>
                </body>
                </html>
                """
            try:
                # Attempt to send the email
                send_mail('Thank you!', thank_you_message, 'allmisizStudent24@gmail.com', [email], html_message=html_message)

                # Redirect to a success page if the email is sent successfully
                return redirect('contact_success')
            except BadHeaderError:
                # Handle the case where there's a bad header in the email
                return HttpResponseServerError('Invalid header found.')
            except Exception as e:
                # Handle other exceptions, such as SMTP connection errors or email delivery failures
                return HttpResponseServerError(f'An error occurred: {e}')
        else:
            # If the form is invalid, re-render the contact page with the form and error messages
            return render(
                request,
                "contact.html",
                {"form": form}  
            )


def contact_success(request):
    """
    Display the success page with thank you message and order content
    """
    
    return render(
        request, 
        'contact_success.html', 
        )