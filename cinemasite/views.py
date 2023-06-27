from django.shortcuts import render
from .models import Film, Genre


def get_films(request):
    films = Film.objects.all()
    context = {
        "films": films
    }
    return render(request, "films.html", context)


