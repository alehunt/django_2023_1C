from django.contrib import admin
from administracion.models import Estudiante, Proyecto, Curso, Categoria, Comision, Inscripcion, Usuario
from django.contrib.auth.admin import UserAdmin 




# # Creacion de un Admin Personalizado heredando de AdminSite
# class CacAdminSite(admin.AdminSite):
#     site_header = 'Administracion Codo a Codo'
#     site_title = 'Administracion superuser'
#     index_title = 'Administracion del sitio'
#     empty_value_display = 'No hay datos para visualizar'

# # Personalizacion de visualizacion de modelos en el Admin de Django


# class EstudianteAdmin(admin.ModelAdmin):
#     list_display = ('matricula', 'nombre', 'apellido', 'dni',)
#     list_editable = ('nombre',)
#     list_filter = ('dni',)
#     search_fields = ('nombre', 'apellido')

# Versión 1: si definimos un modelo intermedio
# class InscripcionInline(admin.TabularInline):
#     model = Inscripcion
#     extra = 1

# # Versión 2:si no tenemos un modelo intermedio (cambia la asociación del inline en admins)
class InscripcionInline(admin.TabularInline):
    model = Comision.estudiantes.through
    extra = 1  # cuantas opciones de carga aparecen por defecto


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'apellido', 'nombre')
    list_display_links = ('nombre', 'apellido', )
    fields = (('nombre', 'apellido'), 'matricula')  # Si no hacemos un valor editable debe manejarse dicha situación de alguna manera.
    # ambas versiones
    inlines = (InscripcionInline, )


class ComisionAdmin(admin.ModelAdmin):
    # ambas versiones
    inlines = (InscripcionInline, )
    # version 2 evitamos doble carga
    exclude = ('estudiantes', )



class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

    # modificacion del listado que se quiere mostrar
    def get_queryset(self, request):
        query = super(CategoriaAdmin, self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query


class CursoAdmin(admin.ModelAdmin):

    # modificar listados de foreingkey
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "categoria":
            kwargs["queryset"] = Categoria.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "anio",  "descripcion")
    prepopulated_fields = {"nombre_slug": ("anio", "nombre")}  # new


# Registro por defecto al admin de Django
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Comision, ComisionAdmin)
admin.site.register(Inscripcion)
admin.site.register(Usuario)

# # registros de modelos en Admin personalizado
# sitio_admin = CacAdminSite(name='cacadmin')
# sitio_admin.register(Estudiante, EstudianteAdmin)
# sitio_admin.register(Proyecto, ProyectoAdmin)
# sitio_admin.register(Categoria, CategoriaAdmin)
# sitio_admin.register(Curso, CursoAdmin)
# sitio_admin.register(Usuario)

