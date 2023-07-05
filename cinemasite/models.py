from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Genre(models.Model):
    """ Model for film genre """
    genre = models.CharField(max_length=30, unique=True)

    # Function taken from Hello Django project:
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

    # Function taken from Hello Django project:
    # https://github.com/ckz8780/ci-fsf-hello-django/blob/9f484408bea5cbc9cc5fb45c0feebc3998ff5f49/todo/models.py
    def __str__(self):
        return self.title


class FilmShowtime(models.Model):
    """ Model for film program """
    rundate = models.DateField(unique=True)
    filmtitle = models.ForeignKey(
        Film, on_delete=models.SET_NULL, null=True, related_name='filmtitle', verbose_name='Film title')
    filmimage = CloudinaryField('image')
    runtime = models.TimeField(unique=True)
    totnumofseats = models.IntegerField(verbose_name='Total number of seats')
    priceperseat = models.FloatField(verbose_name='Price per seat')

    # Function taken from Hello Django project:
    # https://github.com/ckz8780/ci-fsf-hello-django/blob/9f484408bea5cbc9cc5fb45c0feebc3998ff5f49/todo/models.py
    def __str__(self):
        return f"{self.rundate}"


class Snack(models.Model):
    """ Model for snacks that can be added to ticket booking """
    snack = models.CharField(max_length=25, unique=True)
    price = models.FloatField()

    # Function taken from Hello Django project:
    # https://github.com/ckz8780/ci-fsf-hello-django/blob/9f484408bea5cbc9cc5fb45c0feebc3998ff5f49/todo/models.py
    def __str__(self):
        return self.snack


class Booking(models.Model):
    """ Model for ticket booking """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.ForeignKey(FilmShowtime, to_field="rundate", on_delete=models.SET_NULL, null=True, related_name='filmdate')
    filmtitle = models.ForeignKey(Film, to_field="title", on_delete=models.SET_NULL, null=True, verbose_name="Film")
    time = models.ForeignKey(FilmShowtime, to_field="runtime", on_delete=models.SET_NULL, null=True, related_name='filmtime', verbose_name="Runtime")
    numoftickets = models.IntegerField(verbose_name="Number of tickets")
    snacks = models.ForeignKey(Snack, to_field="snack", on_delete=models.SET_NULL, null=True)
    cost = models.IntegerField()

    # Function taken from Hello Django project:
    # https://github.com/ckz8780/ci-fsf-hello-django/blob/9f484408bea5cbc9cc5fb45c0feebc3998ff5f49/todo/models.py
    def __str__(self):
        return f"{self.user}, {self.filmtitle}"
