from django.db import models
from cloudinary.models import CloudinaryField


class Genre(models.Model):
    """ Model for film genre """
    genre = models.CharField(max_length=50, unique=True)

    # Function taken from Hello Django project:
    # https://github.com/ckz8780/ci-fsf-hello-django/blob/9f484408bea5cbc9cc5fb45c0feebc3998ff5f49/todo/models.py
    def __str__(self):
        return self.genre


class Film(models.Model):
    """ Model for film """
    title = models.CharField(max_length=200, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    runtime = models.CharField(max_length=25)
    director = models.CharField(max_length=100)
    cast = models.TextField(max_length=500)
    image = CloudinaryField('image')
    trailer = models.URLField(max_length=300)

    # Function taken from Hello Django project:
    # https://github.com/ckz8780/ci-fsf-hello-django/blob/9f484408bea5cbc9cc5fb45c0feebc3998ff5f49/todo/models.py
    def __str__(self):
        return self.title
