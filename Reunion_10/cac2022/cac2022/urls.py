"""cac2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from hola_mundo.views import hello, index, ola, vista_no_valida
# from hola_mundo import views as vistas_mundo

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', vistas_mundo.vista_no_valida, name="index"),
    # path('hola_mundo/', vistas_mundo.index, name="index"),
    # path('hola_mundo/english', vistas_mundo.hello, name="index"),
    # path('hola_mundo/portugues', vistas_mundo.ola, name="index"),
    path('hola_mundo/', include('hola_mundo.urls')),
]