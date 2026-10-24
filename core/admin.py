from django.contrib import admin
from .models import Pais, Plato, Pelicula

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'pais_origen')

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'director', 'pais')