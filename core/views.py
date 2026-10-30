from django.db.models import Count, Prefetch
from django.shortcuts import get_object_or_404, render

from .models import Pais, Pelicula, Plato


def portada(request):
    paises = Pais.objects.order_by("nombre").prefetch_related(
        Prefetch(
            "platos",
            queryset=(
                Plato.objects.select_related("pais_origen")
                .annotate(num_peliculas=Count("peliculas", distinct=True))
                .order_by("-num_peliculas", "nombre")
            ),
        )
    )

    platos_destacados = []
    for pais in paises:
        platos_del_pais = list(pais.platos.all())
        if platos_del_pais:
            platos_destacados.append(platos_del_pais[0])

    return render(
        request,
        "portada.html",
        {
            "platos_destacados": platos_destacados,
            "total_paises": Pais.objects.count(),
            "total_platos": Plato.objects.count(),
            "total_peliculas": Pelicula.objects.count(),
        },
    )


def lista_platos(request):
    platos = (
        Plato.objects.select_related("pais_origen")
        .annotate(num_peliculas=Count("peliculas", distinct=True))
        .order_by("nombre")
    )
    return render(request, "platos/lista.html", {"platos": platos})


def detalle_plato(request, id):
    plato = get_object_or_404(
        Plato.objects.select_related("pais_origen")
        .annotate(num_peliculas=Count("peliculas", distinct=True))
        .prefetch_related("peliculas__pais"),
        id=id,
    )
    return render(request, "platos/detalle.html", {"plato": plato})


def lista_paises(request):
    paises = (
        Pais.objects.annotate(
            num_platos=Count("platos", distinct=True),
            num_peliculas=Count("peliculas", distinct=True),
        )
        .order_by("nombre")
    )
    return render(request, "paises/lista.html", {"paises": paises})


def detalle_pais(request, id):
    pais = get_object_or_404(
        Pais.objects.prefetch_related("platos", "peliculas"), id=id
    )
    return render(request, "paises/detalle.html", {"pais": pais})


def lista_peliculas(request):
    peliculas = (
        Pelicula.objects.select_related("pais")
        .annotate(num_platos=Count("platos_maridados", distinct=True))
        .order_by("titulo")
    )
    return render(request, "peliculas/lista.html", {"peliculas": peliculas})


def detalle_pelicula(request, id):
    pelicula = get_object_or_404(
        Pelicula.objects.select_related("pais").prefetch_related(
            "platos_maridados__pais_origen"
        ),
        id=id,
    )
    return render(request, "peliculas/detalle.html", {"pelicula": pelicula})
