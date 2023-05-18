from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index_administracion, name='inicio_administracion'),
    # path('categorias/', views.categorias_index, name='categorias_index'),
    path('categorias/', views.CategoriaPepe.as_view(), name='categorias_index'),
    path('categorias/nuevo/', views.categorias_nuevo, name='categorias_nuevo'),
    path('categorias/editar/<int:id_categoria>', views.categorias_editar, name='categorias_editar'),
    path('categorias/eliminar/<int:id_categoria>', views.categorias_eliminar, name='categorias_eliminar'),

    path('cursos/', views.cursos_index, name='cursos_index'),
    path('cursos/nuevo/', views.cursos_nuevo, name='cursos_nuevo'),
    path('cursos/editar/<int:id_curso>', views.cursos_editar, name='cursos_editar'),
    path('cursos/eliminar/<int:id_curso>', views.cursos_eliminar, name='cursos_eliminar'),


    path('categoriasview/', views.CategoriaListView.as_view(), name='categorias_index_view'),
    path('categoriasview/nuevo', views.CategoriaCreateView.as_view(), name='categorias_nuevo_view'),
    path('categoriasview/editar/<int:pk>', views.CategoriaUpdateView.as_view(), name='categorias_editar_view'),
    path('categoriasview/eliminar/<int:pk>', views.CategoriaDeleteView.as_view(), name='categorias_eliminar_view'),

]
