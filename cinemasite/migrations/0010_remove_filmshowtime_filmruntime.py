# Generated by Django 3.2.19 on 2023-07-03 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemasite', '0009_filmshowtime_filmruntime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filmshowtime',
            name='filmruntime',
        ),
    ]
