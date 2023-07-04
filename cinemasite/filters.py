import django_filters
from django import forms
from .models import FilmShowtime


class ShowtimeFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=forms.DateInput(
            attrs={'name': 'date', 'type': 'date', 'class': 'form-control'}), label="")

    class Meta:
        model = FilmShowtime
        fields = ['date']