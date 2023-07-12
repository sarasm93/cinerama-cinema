from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_films, name='home'),
    path('my-bookings', views.view_bookings, name='my-bookings'),
    path('booking', views.view_showtimes, name='booking'),
    path('book/<int:showtime_id>/', views.make_booking, name='book_film'),
    path('edit/<int:booking_id>', views.edit_booking, name='edit'),
    path('cancel/<int:booking_id>', views.cancel_booking, name='cancel'),
]
