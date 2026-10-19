from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from resta.views import restar

urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Ruta para ejecutar la resta con Django
    path('restar/<str:a>/<str:b>/', restar, name='restar'),
    
    # Ruta principal: Carga tu index.html cuando entran al link base
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]