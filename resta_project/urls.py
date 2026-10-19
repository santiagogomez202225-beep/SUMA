from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from resta.views import restar

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Ruta para cuando envían el formulario (ej: /restar/?a=10&b=3)
    path('restar/', restar, name='restar_form'),
    
    # 2. Ruta para cuando escriben los números en la URL (ej: /restar/10/3/)
    path('restar/<str:a>/<str:b>/', restar, name='restar_url'),
    
    # 3. Ruta principal (el index.html)
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]