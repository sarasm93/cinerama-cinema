import django_filters
from django import forms
from .models import FilmShowtime

# Code on lines 9-16, for filtering films based on date, is taken from these
# sites and then altered to fit the project:
# https://www.codechit.com/django-filter-search-form-guide/ ,
# https://forum.djangoproject.com/t/initialize-a-django-filter-with-date/11565,
# https://www.letscodemore.com/blog/customizing-django-filters-with-css-classes/,
# https://forum-djangoproject-com.translate.goog/t/initialize-a-django-filter-with-date/11565?_x_tr_sl=en&_x_tr_tl=sv&_x_tr_hl=sv&_x_tr_pto=sc&_x_tr_hist=true


class ShowtimeFilter(django_filters.FilterSet):
    showtimedate = django_filters.DateFilter(widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control', }),
            label="Choose a date:")

    class Meta:
        model = FilmShowtime
        fields = ['showtimedate', ]
