from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    """ Model for film genre """
    genre = models.CharField(max_length=30, unique=True)

    # The def__str__(self): functions used for the models are taken from the Hello Django project:
    # https://github.com/ckz8780/ci-fsf-hello-django/blob/9f484408bea5cbc9cc5fb45c0feebc3998ff5f49/todo/models.py
    def __str__(self):
        return self.genre


class Film(models.Model):
    """ Model for film """
    title = models.CharField(max_length=100, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    description = models.TextField(unique=True)
    runtime = models.CharField(max_length=25)
    director = models.CharField(max_length=100)
    cast = models.TextField(max_length=500)
    image = CloudinaryField('image')
    trailer = models.URLField(max_length=300)

    def __str__(self):
        return self.title


class FilmShowtime(models.Model):
    """ Model for film program """
    showtimedate = models.DateField(unique=True)
    filmtitle = models.ForeignKey(
        Film, on_delete=models.SET_NULL, null=True, related_name='filmtitle', verbose_name='Film title')
    filmimage = CloudinaryField('image')
    showtime = models.TimeField(max_length=5)
    totnumofseats = models.IntegerField(verbose_name='Total number of seats')
    priceperseat = models.FloatField(verbose_name='Price per seat')

    def __str__(self):
        return f"{self.showtimedate}, {self.filmtitle}"


class Snack(models.Model):
    """ Model for snacks that can be added to ticket booking """
    snack = models.CharField(max_length=25, unique=True)
    price = models.FloatField()

    def __str__(self):
        return self.snack


class Booking(models.Model):
    """ Model for ticket booking """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.ForeignKey(FilmShowtime, to_field="showtimedate", on_delete=models.SET_NULL, null=True, related_name='filmdate')
    time = models.CharField(max_length=20)
    numoftickets = models.IntegerField(validators=[MaxValueValidator(8), MinValueValidator(1)], verbose_name="Number of tickets")
    snacks = models.ForeignKey(Snack, to_field="snack", on_delete=models.SET_NULL, null=True)
    cost = models.FloatField()

    def __str__(self):
        return f"{self.user}, {self.date}"

