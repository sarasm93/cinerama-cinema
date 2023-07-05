from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_films, name='home'),
    path('my-bookings', views.view_bookings, name='my-bookings'),
    path('booking', views.view_showtimes, name='booking'),
    path('edit', views.edit_booking, name='edit'),
]