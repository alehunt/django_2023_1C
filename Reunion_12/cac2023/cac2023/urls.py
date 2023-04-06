from django.contrib import admin
from django.urls import path, include
from hola_mundo import views  as views_hola_mundo

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views_hola_mundo.index),
    path('hola_mundo/', include('hola_mundo.urls')),
]