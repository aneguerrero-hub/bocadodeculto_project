from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Pais, Pelicula, Plato


class CatalogPagesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pais_a = Pais.objects.create(nombre="Italia")
        cls.pais_b = Pais.objects.create(nombre="Japón")

        cls.plato_a = Plato.objects.create(
            nombre="Pasta de prueba",
            descripcion="Una pasta para comprobar las fichas del catálogo.",
            precio=Decimal("12.50"),
            pais_origen=cls.pais_a,
        )
        cls.plato_b = Plato.objects.create(
            nombre="Pizza de prueba",
            descripcion="Una pizza para comprobar la selección de portada.",
            precio=Decimal("10.00"),
            pais_origen=cls.pais_a,
        )
        cls.plato_c = Plato.objects.create(
            nombre="Ramen de prueba",
            descripcion="Un ramen para el segundo país.",
            precio=Decimal("13.00"),
            pais_origen=cls.pais_b,
        )

        cls.pelicula_a = Pelicula.objects.create(
            titulo="Película uno",
            sinopsis="Sinopsis de prueba uno.",
            director="Directora uno",
            pais=cls.pais_a,
        )
        cls.pelicula_b = Pelicula.objects.create(
            titulo="Película dos",
            sinopsis="Sinopsis de prueba dos.",
            director="Director dos",
            pais=cls.pais_b,
        )
        cls.pelicula_a.platos_maridados.add(cls.plato_a, cls.plato_b)
        cls.pelicula_b.platos_maridados.add(cls.plato_a, cls.plato_c)

    def test_all_public_list_and_detail_routes_render(self):
        paths = [
            reverse("portada"),
            reverse("lista_platos"),
            reverse("detalle_plato", args=[self.plato_a.pk]),
            reverse("lista_paises"),
            reverse("detalle_pais", args=[self.pais_a.pk]),
            reverse("lista_peliculas"),
            reverse("detalle_pelicula", args=[self.pelicula_a.pk]),
        ]
        for path in paths:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, "Bocado de Culto")

    def test_home_selects_one_dish_per_country_and_prioritizes_film_count(self):
        response = self.client.get(reverse("portada"))
        self.assertEqual(response.status_code, 200)
        selected = response.context["platos_destacados"]
        self.assertEqual(len(selected), 2)
        selected_names = {plato.nombre for plato in selected}
        self.assertEqual(selected_names, {"Pasta de prueba", "Ramen de prueba"})

    def test_related_links_connect_dishes_countries_and_films(self):
        dish_response = self.client.get(reverse("detalle_plato", args=[self.plato_a.pk]))
        country_response = self.client.get(reverse("detalle_pais", args=[self.pais_a.pk]))
        movie_response = self.client.get(reverse("detalle_pelicula", args=[self.pelicula_a.pk]))

        self.assertContains(dish_response, reverse("detalle_pais", args=[self.pais_a.pk]))
        self.assertContains(dish_response, reverse("detalle_pelicula", args=[self.pelicula_a.pk]))
        self.assertContains(country_response, reverse("detalle_plato", args=[self.plato_a.pk]))
        self.assertContains(movie_response, reverse("detalle_plato", args=[self.plato_a.pk]))

    def test_template_stylesheets_are_linked(self):
        response = self.client.get(reverse("lista_platos"))
        self.assertContains(response, "/static/css/base.css")
        self.assertContains(response, "/static/css/platos.css")
