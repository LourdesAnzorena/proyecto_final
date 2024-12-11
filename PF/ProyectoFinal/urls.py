"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import os
import sys

# Añade el directorio de tu proyecto al PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Establece el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoFinal.settings')

# Importa Django y configura la aplicación
import django
django.setup()

from django.contrib import admin
from django.urls import path
from ProyectoFinal.view import saludo, diadehoy  # Importa usando un punto

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('saludo/', saludo),         # URL para la vista 'saludo'
    path('diadehoy/', diadehoy),     # URL para la raíz del sitio
]
