from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada, name='portada'),
    path('paises/', views.lista_paises, name='lista_paises'),
    path('paises/<int:id>/', views.detalle_pais, name='detalle_pais'),
    path('peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('peliculas/<int:id>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('platos/', views.lista_platos, name='lista_platos'),
    path('platos/<int:id>/', views.detalle_plato, name='detalle_plato'),
]

