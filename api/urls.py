"""
URL configuration for api_rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter

app_name = 'api'  # Define o namespace para as URLs da API

router = DefaultRouter()
router.register('usuarios', views.UsuariosViewSet, basename='usuarios')  # Registra o viewset com o nome 'usuarios'

# Define as URLs para o aplicativo 'api'
# As URLs são mapeadas para as views correspondentes
urlpatterns = [
    #path('cadastrar/', views.form_cadastro_view, name='form_cadastro'),  # <--- ESTE É O NOME DA URL "cadastro"
    path('consultar/', views.consulta_view, name='consulta'),  # <--- ESTE É O NOME DA URL "consulta"
   
    # Inclui as URLs do router para a API REST
    path('adicionar/',views.cadastro_view, name='adicionar'),  # <--- ESTE É O NOME DA URL "adicionar"
    path('api/', include(router.urls)),
]
