from django.shortcuts import render, redirect
from .models import Film, Genre
# from .forms import CustomerForm
from django.contrib import messages


def get_films(request):
    films = Film.objects.all()
    context = {
        "films": films
    }
    return render(request, "films.html", context)

"""
def register_customer(request):
    if request.method == "POST":
        registration_form = CustomerForm(request.POST)  
        if registration_form.is_valid():
            registration_form.save()
            return redirect("home")  
            messages.success(request, 'Your account was registered successfully!')
        else:
            messages.error('wrong')
    registration_form = CustomerForm()  
    context = {
        "registration_form": registration_form
    }
    return render(request, "registration.html", context)
   """ 