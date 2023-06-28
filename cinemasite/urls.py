from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_films, name='home'),
    path('registration', views.get_registration_form, name='registration')
]