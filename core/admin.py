from django.contrib import admin
from .models import Categoria, Plato, Pelicula

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'director', 'plato_maridado')
    search_fields = ('titulo', 'director')