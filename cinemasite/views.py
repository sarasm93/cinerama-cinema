from django.shortcuts import render, redirect
from .models import Film, FilmShowtime, Booking, Snack
from django.contrib import messages
from .filters import ShowtimeFilter


def get_films(request):
    films = Film.objects.all()
    context = {
        'films': films
    }
    return render(request, 'films.html', context)


"""def book_tickets(request):
    showtimes = FilmShowtime.objects.all()
    context = {
        'showtimes': showtimes,
    }
    return render(request, 'booking.html', context)"""


def view_bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'profile.html', context)


def view_showtimes(request):
    showtimes = FilmShowtime.objects.all()
    myfilter = ShowtimeFilter(request.GET, queryset=showtimes)
    showtimes = myfilter.qs
    snacks = Snack.objects.all()
    context = {
        'myfilter': myfilter,
        'showtimes': showtimes,
        'snacks': snacks,
        }
    return render(request, 'booking.html', context)

