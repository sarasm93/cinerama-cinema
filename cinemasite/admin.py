from django.contrib import admin
from .models import Film, Genre, FilmShowtime, Booking, Snack

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(FilmShowtime)
admin.site.register(Booking)
admin.site.register(Snack)

