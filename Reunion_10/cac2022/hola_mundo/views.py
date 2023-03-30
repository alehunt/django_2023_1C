from django.http import HttpResponse


def vista_no_valida(request):
    return HttpResponse("No es una url válida")


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hola gente</h1>")


def hello(request):
    return HttpResponse("Hello world")


def ola(request):
    return HttpResponse("Olá mundo")


def saludar(request, primer_nombres):
    return HttpResponse(f"Hola {primer_nombres.upper()}")
