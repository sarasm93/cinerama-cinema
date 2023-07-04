# Generated by Django 3.2.19 on 2023-07-03 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemasite', '0005_auto_20230703_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmshowtime',
            name='filmimage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='filmimage', to='cinemasite.film'),
        ),
        migrations.AlterField(
            model_name='filmshowtime',
            name='filmtitle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='filmtitle', to='cinemasite.film'),
        ),
    ]