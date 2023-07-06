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


def make_booking(request, showtime_id):
    def calculate_price(number_of_tickets, priceperseat, snack_price):
        return (priceperseat * int(number_of_tickets)) + snack_price

    print(request.POST)
    film_showtime = FilmShowtime.objects.get(pk=showtime_id)
    if request.method == "POST":
        #user = request.user.email
        #date = request.POST.get("date")
        # filmtitle = request.POST.get("filmtitle")
        # filmtitle = movie_id
        #time = request.POST.get("time")
        numoftickets = request.POST.get("numoftickets")
        snacks = Snack.objects.get(pk=request.POST.get("snacks"))
        # cost = request.POST.get("cost")
        cost = calculate_price(numoftickets, film_showtime.priceperseat, snacks.price)
        booking = Booking.objects.create(user=request.user, date=film_showtime, filmtitle=film_showtime.filmtitle, time=film_showtime, numoftickets=numoftickets, snacks=snacks, cost=cost)
        return redirect("my-bookings")
    return render(request, "booking.html")


def edit_booking(request, booking_id):
    # snacks = Snack.objects.all()
    # context = {
    #     'snacks': snacks,
    # }
    booking = get_object_or_404(Booking, id=booking_id)
    context = {
        'booking': booking,
    }
    return render(request, 'edit.html', context)