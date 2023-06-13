"""pig_23320 URL Configuration

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
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
# from administracion.admin import sitio_admin # Se debe cargar en admin.py

urlpatterns = [
    path('api/', include('recursos_api.urls')),
    path('', include('portal.urls')),
    path('admin/', admin.site.urls),
    # path('sitio_admin/', sitio_admin.urls), # Se debe cargar en admin.py
    path('administracion/', include('administracion.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
