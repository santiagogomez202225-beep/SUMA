from django.contrib import admin
from django.urls import path
from resta.views import restar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restar/<str:a>/<str:b>/', restar, name='restar'),
]