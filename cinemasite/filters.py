import django_filters
from django import forms
from .models import FilmShowtime


class ShowtimeFilter(django_filters.FilterSet):
    showtimedate = django_filters.DateFilter(widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control', }),
            label="Choose a date:")

    class Meta:
        model = FilmShowtime
        fields = ['showtimedate', ]
