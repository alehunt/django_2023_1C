# nuestro propio sitio admin
from django.contrib import admin
from cac.models import Estudiante, Docente, Curso, Comision, Inscripcion

class CacAdminSite(admin.AdminSite):
    site_header = "Administración de Codo a Codo"
    site_title = "Administración para super usuarios"
    index_title = "Administrador del Sitio"
    empty_value_display = "No hay nada"

# Versión 1: si definimos un modelo intermedio
# class InscripcionInline(admin.TabularInline):
#     model = Inscripcion
#     extra = 1

# # Versión 2:si no tenemos un modelo intermedio (cambia la asociación del inline en admins)
class InscripcionInline(admin.TabularInline):
    model = Comision.estudiantes.through
    extra = 1  # cuantas opciones de carga aparecen por defecto

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('legajo', 'apellido', 'nombre')
    list_display_links = ('nombre', 'apellido', )
    fields = (('nombre', 'apellido'), 'legajo')  # Si no hacemos un valor editable debe manejarse dicha situación de alguna manera.
    # ambas versiones
    inlines = (InscripcionInline, )


class ComisionAdmin(admin.ModelAdmin):
    # ambas versiones
    inlines = (InscripcionInline, )
    # version 2 evitamos doble carga
    exclude = ('estudiantes', )


sitio_admin = CacAdminSite(name='cacadmin')
sitio_admin.register(Estudiante, EstudianteAdmin)
sitio_admin.register(Docente)
sitio_admin.register(Curso)
sitio_admin.register(Comision, ComisionAdmin)
sitio_admin.register(Inscripcion)


# # Sobreescribiendo el sitio de admin por defecto
# from django.contrib import admin
# from .models import Estudiante, Docente, Curso, Comision, Inscripcion
# from .forms import DocenteForm


# class EstudianteAdmin(admin.ModelAdmin):
#     list_display = ('legajo', 'apellido', 'nombre')
#     list_editable = ('apellido', 'nombre')
#     list_display_links = ('legajo',)
#     search_fields = ['apellido']


# # admin.site.register(Estudiante, EstudianteAdmin)


# class DocenteAdmin(admin.ModelAdmin):
#     form = DocenteForm


# @admin.display(description='Nombre del curso en mayuscula')
# def curso_mayuscula(objeto):
#     return f"Curso {objeto.nombre}".upper()


# @admin.register(Curso)
# class CursoAdmin(admin.ModelAdmin):
#     # formfield_overrides = {
#     #     models.TextField: {'widget': widgets.CacTextWidget}
#     # }
#     list_display = (curso_mayuscula, 'curso_minuscula', )

#     @admin.display(description='Nombre del curso en minuscula')
#     def curso_minuscula(self, objeto):
#         return f"Curso {objeto.nombre}".lower()


# # @admin.register(Comision)
# class ComisionAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'fecha_inicio', )

#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         if db_field.name == "estudiantes":
#             kwargs["queryset"] = Estudiante.objects.filter(legajo__startswith="2").order_by("apellido")
#         return super().formfield_for_manytomany(db_field, request, **kwargs)


# @admin.register(Inscripcion)
# class InscripcionAdmin(admin.ModelAdmin):
#     pass


# # Register your models here.
# admin.site.register(Estudiante, EstudianteAdmin)
# admin.site.register(Docente, DocenteAdmin)
# admin.site.register(Comision, ComisionAdmin)
