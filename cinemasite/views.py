from django.shortcuts import render, redirect, get_object_or_404
from .models import Film, FilmShowtime, Booking, Snack
from django.contrib import messages
from .filters import ShowtimeFilter


def get_films(request):
    films = Film.objects.all()
    context = {
        'films': films
    }
    return render(request, 'films.html', context)


def view_bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'my-bookings.html', context)


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


def make_booking(request):
    if request.method == "POST":
        user = request.user.email
        date = request.POST.get("date")
        filmtitle = request.POST.get("filmtitle")
        time = request.POST.get("time")
        numoftickets = request.POST.get("numoftickets")
        snacks = request.POST.get("snacks")
        cost = request.POST.get("cost")
        booking = Booking.objects.create(user=user, date=date, filmtitle=filmtitle, time=time, numoftickets=numoftickets, snacks=snacks, cost=cost)
        return redirect("my-bookings")
    return render(request, "booking.html")


def edit_booking(request):
    snacks = Snack.objects.all()
    context = {
        'snacks': snacks,
    }
    # booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'edit.html', context)