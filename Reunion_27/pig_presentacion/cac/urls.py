from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('quienessomos/', views.quienes_somos, name='quienes_somos'),
    path('proyectos/', views.ver_proyectos, name='proyectos'),
    path('cursos/', views.ver_cursos, name='cursos'),
    path('administracion', views.index_administracion, name='inicio_administracion'),
    path('api_proyectos/', views.api_proyectos, name="api_proyectos"),

    path('hola_mundo', views.hola_mundo),
    path('saludarbonito/', views.saludar, name="saludar_por_defecto"),
    path('saludar/<str:nombre>', views.saludar, name="saludar"),
    # path('proyectos/2022/07',views.ver_proyectos_2022_07),
    # re_path(r'^proyectos/(?P<anio>\d{2,4})/$',views.ver_proyectos),
    # path('proyectos/<int:anio>/<int:mes>',views.ver_proyectos,name="ver_proyectos"),
    # path('cursos/detalle/<slug:nombre_curso>',views.cursos_detalle, name="curso_detalle"),
    # re_path(r'^cursos/(?P<nombre>\w+)/$',views.cursos,name="cursos")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
