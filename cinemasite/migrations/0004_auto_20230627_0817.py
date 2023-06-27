# Generated by Django 3.2.19 on 2023-06-27 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemasite', '0003_alter_film_cast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='cinemasite.Genre'),
        ),
    ]
