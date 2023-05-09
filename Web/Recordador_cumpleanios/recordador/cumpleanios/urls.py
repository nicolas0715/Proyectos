from django.urls import path
from .views import index, agregar, ver_mas, buscar


urlpatterns = [
    path('', index),
    path('agregar/', agregar),
    path('ver_mas/', ver_mas),
    path('buscar/', buscar),
]