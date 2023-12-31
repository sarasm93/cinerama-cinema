# Generated by Django 3.2.19 on 2023-07-13 16:55

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(unique=True)),
                ('runtime', models.CharField(max_length=25)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.TextField(max_length=500)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('trailer', models.URLField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snack', models.CharField(max_length=25, unique=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FilmShowtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showtimedate', models.DateField()),
                ('filmimage', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('showtime', models.TimeField(max_length=5)),
                ('priceperseat', models.FloatField(verbose_name='Price per seat')),
                ('filmtitle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='filmtitle', to='cinemasite.film', verbose_name='Film title')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinemasite.genre'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(max_length=10)),
                ('numoftickets', models.IntegerField(validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)], verbose_name='Number of tickets')),
                ('cost', models.FloatField()),
                ('date', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='filmdate', to='cinemasite.filmshowtime')),
                ('snacks', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinemasite.snack', to_field='snack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
