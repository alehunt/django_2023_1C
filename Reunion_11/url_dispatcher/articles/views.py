from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def special_case_2003(request):
    return HttpResponse("Caso especial del 2003")


def year_archive(request, year):
    return HttpResponse(f"Archivos el año {year}")


def month_archive(request, year, month):
    return HttpResponse(f"Archivos del mes {month} del año {year}")


def article_detail(request, year, month, slug):
    return HttpResponse(f"Detalle del archivo con slug '{slug}' del mes {month} del año {year}")