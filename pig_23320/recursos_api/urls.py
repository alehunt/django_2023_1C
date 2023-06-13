from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recursos_api import views

juan = DefaultRouter()
juan.register('estudiantes', viewset=views.EstudianteViewSet, basename='estudiante')

urlpatterns = [
    path('', include(juan.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]

