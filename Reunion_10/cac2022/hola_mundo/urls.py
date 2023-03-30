from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('english', views.hello, name="hello"),
    path('portuguese', views.ola, name='ola'),
    path('saludar/<str:primer_nombres>', views.saludar, name="saludar"),
    ]
