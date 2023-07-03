from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_films, name='home'),
    path('profile', views.view_bookings, name='profile'),
    path('booking', views.book_tickets, name='booking')
]