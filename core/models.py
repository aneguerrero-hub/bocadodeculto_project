from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='platos')

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=150)
    sinopsis = models.TextField()
    director = models.CharField(max_length=100)
    plato_maridado = models.ForeignKey(Plato, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo