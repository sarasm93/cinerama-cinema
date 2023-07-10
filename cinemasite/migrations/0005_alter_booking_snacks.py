# Generated by Django 3.2.19 on 2023-07-10 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemasite', '0004_alter_booking_snacks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='snacks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinemasite.snack', to_field='snack'),
        ),
    ]
