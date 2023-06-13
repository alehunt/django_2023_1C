from administracion.models import Estudiante
from rest_framework import serializers


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
