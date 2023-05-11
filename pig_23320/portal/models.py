from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)