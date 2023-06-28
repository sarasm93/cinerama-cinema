from django import forms
from .models import Customer


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'email', 'phone_number', 'password']