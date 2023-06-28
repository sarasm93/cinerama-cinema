from django.shortcuts import render
from .models import Film, Genre
from .forms import RegistrationForm


def get_films(request):
    films = Film.objects.all()
    context = {
        "films": films
    }
    return render(request, "films.html", context)


# Code on line 16-25 for registration form is taken from the Hello Django 
# project (see link below) and altered to fit this project.
# https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/22da66e7007d4b5a9bd53901c84034e8/?child=first
def get_registration_form(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("get_films")
    form = RegistrationForm()
    context = {
        "form": form
    }
    return render(request, "registration.html", context)

