from django.shortcuts import render, redirect
from .models import Film, FilmShowtime, Booking
from django.contrib import messages


def get_films(request):
    films = Film.objects.all()
    context = {
        'films': films
    }
    return render(request, 'films.html', context)


def book_tickets(request):
    showtimes = FilmShowtime.objects.all()
    films = Film.objects.all()
    context = {
        'showtimes': showtimes,
        'films': films
    }
    return render(request, 'booking.html', context)


def view_bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'profile.html', context)

