# Generated by Django 3.2.19 on 2023-06-27 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemasite', '0005_remove_film_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cinemasite.genre'),
        ),
    ]
