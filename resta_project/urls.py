from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from resta.views import restar

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta para el formulario
    path('restar/', restar, name='restar_form'),
    
    # Ruta por si escriben los números directo en la URL
    path('restar/<str:a>/<str:b>/', restar, name='restar_url'),
    
    # Ruta principal: carga el HTML de la carpeta public
    path('', TemplateView.as_view(template_name='public/index.html'), name='home'),
]