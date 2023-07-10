from django.shortcuts import render, redirect, get_object_or_404
from .models import Film, FilmShowtime, Booking, Snack
from .forms import BookingForm
from django.contrib import messages
from .filters import ShowtimeFilter


def get_films(request):
    films = Film.objects.all()
    context = {
        'films': films
    }
    return render(request, 'films.html', context)


def view_showtimes(request):
    showtimes = FilmShowtime.objects.all()
    myfilter = ShowtimeFilter(request.GET, queryset=showtimes)
    showtimes = myfilter.qs
    snacks = Snack.objects.all() 
    context = {
        'myfilter': myfilter,
        'showtimes': showtimes,
        'snacks': snacks,
        'booking_form': BookingForm(),
    }
    return render(request, 'booking.html', context)


def make_booking(request, showtime_id):
    def calculate_price(number_of_tickets, priceperseat, snack_price):
        return (priceperseat * int(number_of_tickets)) + snack_price

    film_showtime = FilmShowtime.objects.get(pk=showtime_id)
    booking_form = BookingForm(data=request.POST)

    if booking_form.is_valid():
        booking_form.instance.user = request.user
        booking_form.instance.date = film_showtime
        booking_form.instance.time = film_showtime.showtime
        booking = booking_form.save(commit=False)
        booking.cost = calculate_price(booking.numoftickets, film_showtime.priceperseat, booking.snacks.price)
        booking_form.save()
    else:
        return redirect("booking")

    bookings = Booking.objects.all()
    return render(request, 'my-bookings.html', {'bookings': bookings})        


def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {
        'bookings': bookings
    }
    return render(request, 'my-bookings.html', context)


def edit_booking(request, booking_id):
    def calculate_price(number_of_tickets, priceperseat, snack_price):
        return (priceperseat * int(number_of_tickets)) + snack_price
    
    booking = get_object_or_404(Booking, id=booking_id)
    snacks = Snack.objects.all()
    context = {
        'booking': booking,
        'snacks': snacks,
        'booking_form': BookingForm(instance=booking, initial={'numoftickets': booking.numoftickets, 'snacks': booking.snacks}),
    }
    return render(request, 'edit.html', context)

    booking_form = BookingForm(data=request.POST, instance=booking)
    film_showtime = FilmShowtime.objects.get(pk=showtime_id)

    if booking_form.is_valid():
        updated_booking = booking_form.save(commit=False)
        updated_booking.cost = calculate_price(updated_booking.numoftickets, film_showtime.priceperseat, updated_booking.snacks.price)
        updated_booking.save()
        return redirect('my-bookings')

    
