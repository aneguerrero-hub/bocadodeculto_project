from django.shortcuts import render, get_object_or_404
from .models import Plato, Pais, Pelicula

def portada(request):
    paises = Pais.objects.all()
    platos_destacados = []
    for pais in paises:
        # Cambiado 'pais' por 'pais_origen'
        plato = Plato.objects.filter(pais_origen=pais).first()
        if plato:
            platos_destacados.append(plato)
    return render(request, 'portada.html', {'platos_destacados': platos_destacados})

def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'platos/lista.html', {'platos': platos})

def detalle_plato(request, id):
    plato = get_object_or_404(Plato, id=id)
    return render(request, 'platos/detalle.html', {'plato': plato})

def lista_paises(request):
    paises = Pais.objects.all().order_by("nombre")
    return render(request, "paises/lista.html", {"paises": paises})

def lista_peliculas(request):
    peliculas = Pelicula.objects.all().order_by("titulo")
    return render(request, "peliculas/lista.html", {"peliculas": peliculas})

def detalle_pais(request, id):
    pais = get_object_or_404(Pais, id=id)
    return render(request, "paises/detalle.html", {"pais": pais})

def detalle_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, "peliculas/detalle.html", {"pelicula": pelicula})