from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from resta.views import restar

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Ruta para el formulario (cuando el usuario da clic en "Restar")
    path('restar/', restar, name='restar_form'),
    
    # 2. Ruta manual (por si escriben los números en la URL)
    path('restar/<str:a>/<str:b>/', restar, name='restar_url'),
    
    # 3. Página principal: Carga tu HTML de la carpeta public
    path('', TemplateView.as_view(template_name='public/index.html'), name='home'),
]