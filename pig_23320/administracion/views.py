from django.shortcuts import render

# Create your views here.
def index_administracion(request):
    variable = 'test variable'
    return render(request, 'administracion/index.html', {'variable': variable})
