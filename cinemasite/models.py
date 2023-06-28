from django.db import models
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
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
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
    date = models.DateField()
    film_title = models.ForeignKey(Film, on_delete=models.CASCADE)
    time = models.TimeField()
    tot_num_of_seats = models.IntegerField()
    price_per_seat = models.IntegerField()

    # Function taken from Hello Django project:
    # https://github.com/ckz8780/ci-fsf-hello-django/blob/9f484408bea5cbc9cc5fb45c0feebc3998ff5f49/todo/models.py
    def __str__(self):
        return self.date.film_title.time


class Customer(models.Model):
    """ Model for customer registration and login """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=20)

    # Function taken from Hello Django project:
    # https://github.com/ckz8780/ci-fsf-hello-django/blob/9f484408bea5cbc9cc5fb45c0feebc3998ff5f49/todo/models.py
    def __str__(self):
        return self.email
