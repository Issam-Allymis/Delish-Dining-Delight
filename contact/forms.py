from django import forms
from .models import Contact  

class ContactForm(forms.ModelForm):  # Use ModelForm
    class Meta:
        model = Contact
        fields = ['name', 'email', 'address', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'style': 'width: 500px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'width: 500px;'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address', 'style': 'width: 500px;'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Place Your Order', 'rows': '8', 'cols': '20'}),
        }