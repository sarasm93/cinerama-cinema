from django import forms
from .models import Customer
from django.forms import TextInput, PasswordInput


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'email', 'phone_number', 'password']
        widgets = {
            'phone_number': TextInput,            
        }


class Login(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'password']
        widgets = {
            'password': PasswordInput            
        }
