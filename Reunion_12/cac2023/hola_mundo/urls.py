from django.urls import path
from . import views

urlpatterns = [
    path('pepe', views.saludo, name="saludo"),
]
