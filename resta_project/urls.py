from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
# Importamos AMBAS funciones del views
from resta.views import restar, sumar 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas para Restar
    path('restar/', restar, name='restar_form'),
    path('restar/<str:a>/<str:b>/', restar, name='restar_url'),
    
    # Rutas para Sumar
    path('sumar/', sumar, name='sumar_form'),
    path('sumar/<str:a>/<str:b>/', sumar, name='sumar_url'),
    
    # Página principal (el index.html)
    path('', TemplateView.as_view(template_name='public/index.html'), name='home'),
]