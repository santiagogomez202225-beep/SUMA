from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from resta.views import restar

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ruta para hacer la resta
    path('restar/<str:a>/<str:b>/', restar, name='restar'),
    # Ruta principal: carga el HTML que está dentro de la carpeta public
    path('', TemplateView.as_view(template_name='public/index.html'), name='home'),
]