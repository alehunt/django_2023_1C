from django.shortcuts import render, redirect
from django.views.generic import ListView
from administracion.forms import CategoriaForm
from administracion.models import Categoria, Curso


# Create your views here.


def index_administracion(request):
    variable = 'test variable'
    return render(request, 'administracion/index_administracion.html', {'variable': variable})


"""
    CRUD Categorias
"""


class CategoriaPepe(ListView):
    model = Categoria
    template_name = 'administracion/categorias/index.html'
    context_object_name = 'categorias'
    queryset = Categoria.objects.filter(baja=False)



# def categorias_index(request):
#     # queryset
#     categorias = Categoria.objects.filter(baja=False)
#     return render(request, 'administracion/categorias/index.html', {'categorias': categorias})


def categorias_nuevo(request):
    if (request.method == 'POST'):
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            categoria = Categoria(nombre=nombre)
            categoria.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm()
    return render(request, 'administracion/categorias/nuevo.html', {'formulario': formulario})


def categorias_editar(request, id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    if (request.method == 'POST'):
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            categoria.nombre = formulario.cleaned_data['nombre']
            categoria.save()
            return redirect('categorias_index')
    else:
        formulario = CategoriaForm(initial={'nombre': categoria.nombre})
    return render(request, 'administracion/categorias/editar.html', {'formulario': formulario})


def categorias_eliminar(request, id_categoria):
    try:
        categoria = Categoria.objects.get(pk=id_categoria)
    except Categoria.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    categoria.soft_delete()
    return redirect('categorias_index')
