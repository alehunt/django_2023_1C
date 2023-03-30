
from django.urls import path
from . import views

urlpatterns = [
    path('saludar/<int:edad>', views.saludar),
    path('saludar/english', views.saludar_english),
    path('saludar/french', views.saludar_english),
]
