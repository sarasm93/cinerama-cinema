# Generated by Django 3.2.19 on 2023-07-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemasite', '0002_alter_filmshowtime_showtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmshowtime',
            name='showtime',
            field=models.TimeField(blank=True, max_length=5, null=True),
        ),
    ]