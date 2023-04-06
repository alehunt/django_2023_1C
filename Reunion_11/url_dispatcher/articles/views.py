from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest


def index(request):
    return render(request, "index.html")


# Create your views here.
def special_case_2003(request):
    return HttpResponse("Caso especial del 2003")


def year_archive(request, year):
    if year <= 2023:
        return HttpResponse(f"Archivos el año {year}")
    else:
        url  = reverse('articles-index')
        return HttpResponseRedirect(url)
    # return HttpResponse(f"Archivos el año {year}")


def month_archive(request, year, month):
    variable = request.GET['montoto']
    return HttpResponse(f"Archivos del mes {month} del año {year}")


def article_detail(request, year, month, slug):
    return HttpResponse(f"Detalle del archivo con slug '{slug}' del mes {month} del año {year}")