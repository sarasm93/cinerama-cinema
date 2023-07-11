from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from .models import Booking, Snack, FilmShowtime


# Code on line 9-18 taken from the below Geeksforgeeks.org page, to add first 
# name and last name to allauth signup form:
# https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30, label='First Name', widget=forms.TextInput(
            attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(
        max_length=30, label='Last Name', widget=forms.TextInput(
            attrs={'placeholder': 'Last name'}))
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)  
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['numoftickets', 'snacks']