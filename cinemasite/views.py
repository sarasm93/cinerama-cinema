from django.shortcuts import render


def get_base(request):
    return render(request, "cinemasite/base.html")
