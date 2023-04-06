from datetime import datetime
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     template = loader.get_template('hola_mundo/index.html')
#     context = {}
#     return HttpResponse(template.render(context, request))


# def saludo(request):
#     template = loader.get_template('hola_mundo/saludo.html')
#     context = {"ahora": datetime.now}
#     return HttpResponse(template.render(context, request))


def saludo(request):
    dicccionario = {
        'ahora': datetime.now,
        'mañana': "el dia de mañana"
    }
    return render(request, "hola_mundo/saludo.html", dicccionario)


def index(request):
    return render(request, "hola_mundo/index.html",  {})

