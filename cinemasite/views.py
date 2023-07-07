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

    print(request.POST)
    film_showtime = FilmShowtime.objects.get(pk=showtime_id)
    booking_form = BookingForm(data=request.POST)
    
    if booking_form.is_valid():
    # numoftickets = request.POST.get("numoftickets")
    # snacks = Snack.objects.get(pk=request.POST.get("snacks"))
        booking_form.instance.user = request.user
        booking_form.instance.date = film_showtime.date
        booking = booking_form.save(commit=False)
        booking.cost = calculate_price(numoftickets, film_showtime.priceperseat, snacks.price)
        booking_form.save()
    # booking = Booking.objects.create(user=request.user, date=film_showtime, filmtitle=film_showtime.filmtitle, time=film_showtime, numoftickets=numoftickets, snacks=snacks, cost=cost)
    else:
        booking_form = BookingForm()

    return render(request, "films.html")


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
    }
    if request.method == 'POST':
        booking.numoftickets = request.POST.get('numoftickets')
        booking.snacks = request.POST.get("snacks")
        booking.save()
        return redirect('my-bookings')
    return render(request, 'edit.html', context)
