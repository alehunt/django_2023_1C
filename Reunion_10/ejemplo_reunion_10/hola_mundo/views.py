from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def saludar(request, edad=20):
    return HttpResponse(f"<h1>Sos re viejo tenes {edad} años</h1>")


def saludar_english(request):
    return HttpResponse("Hello")
