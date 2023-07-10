# Generated by Django 3.2.19 on 2023-07-10 10:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemasite', '0003_alter_filmshowtime_showtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='numoftickets',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)], verbose_name='Number of tickets'),
        ),
    ]