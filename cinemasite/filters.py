import django_filters
from django import forms
from .models import FilmShowtime


class ShowtimeFilter(django_filters.FilterSet):
    rundate = django_filters.DateFilter(widget=forms.DateInput(
            attrs={'name': 'rundate', 'type': 'date', 'class': 'form-control'}), label="")

    class Meta:
        model = FilmShowtime
        fields = ['rundate', ]