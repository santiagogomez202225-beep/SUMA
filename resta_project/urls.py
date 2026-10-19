from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from resta.views import restar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restar/<str:a>/<str:b>/', restar, name='restar'),
    # Le decimos que busque el index.html dentro de public
    path('', TemplateView.as_view(template_name='public/index.html'), name='home'),
]