from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    pais_origen = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='platos')

    class Meta:
        verbose_name = "Plato"
        verbose_name_plural = "Platos"

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=150)
    sinopsis = models.TextField()
    director = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='peliculas')
    platos_maridados = models.ManyToManyField(Plato, related_name='peliculas')

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"

    def __str__(self):
        return self.titulo