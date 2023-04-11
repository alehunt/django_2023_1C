from django.urls import path
from . import views

urlpatterns = [
    path('pepe', views.saludo_idiomas, name="saludo"),
]
