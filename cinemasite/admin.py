from django.contrib import admin
from .models import Film, Genre, FilmShowtime

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(FilmShowtime)
