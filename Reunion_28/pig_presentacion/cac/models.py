from email.policy import default
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _


class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')

    class Meta:
        abstract = True


class Estudiante(Persona):
    class Meta:
        verbose_name_plural = _("Estudiantes")
    legajo = models.CharField(max_length=100, verbose_name='Legajo')

    def __str__(self):
        return f"{self.legajo} - {self.apellido}, {self.nombre}"


class Docente(Persona):
    class Meta:
        verbose_name_plural = _("Docentes")
    cuit = models.CharField(max_length=100, verbose_name='Cuit')


class Curso(models.Model):
    class Meta:
        verbose_name_plural = _("Cursos")
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    baja = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def soft_delete(self):
        self.baja = True
        self.save()

    def restore(self):
        self.baja = False
        self.save()


class Comision(models.Model):
    class Meta:
        verbose_name_plural = _("Comisiones")

    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    portada = models.ImageField(upload_to='imagenes/comisiones/', null=True, verbose_name='Portada', default=None)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    # version 1 admin
    estudiantes = models.ManyToManyField(Estudiante, through='Inscripcion')
    # version 2 admin
    # estudiantes = models.ManyToManyField(Estudiante)

    def __str__(self):
        return self.nombre

    def delete(self, using=None, keep_parents=False):
        self.portada.storage.delete(self.portada.name)  # borrado fisico de la imagen
        super().delete()


class Inscripcion(models.Model):
    class Meta:
        verbose_name_plural = _("Inscripciones")

    class Estado(models.IntegerChoices):
        INSCRIPTO = 1
        CURSANDO = 2
        EGRESADO = 3

    fecha_creacion = models.DateField(verbose_name='Fecha de creación')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    comision = models.ForeignKey(Comision, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=Estado.choices, default=Estado.INSCRIPTO)
    # opción sin crear la clase interna Estado
    # estado = models. IntegerChoices("Estado", 'INSCRIPTO CURSANDO EGRESADO')

    def __str__(self):
        return self.id
