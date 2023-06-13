from rest_framework import viewsets, permissions
from administracion.models import Estudiante
from recursos_api.serializers import EstudianteSerializer
from django.shortcuts import render


# Create your views here.
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]