# Bocado de Culto

Proyecto web colaborativo en Django para explorar la relación entre platos, países y películas.

## Requisitos

- Python 3.10 o superior compatible con la versión de Django instalada.
- Django (la versión utilizada en el entorno de desarrollo del proyecto es 6.1.2).

## Puesta en marcha

Desde la carpeta que contiene `manage.py`:

```bash
py manage.py migrate
py manage.py runserver
```

Después, abre `http://127.0.0.1:8000/`. El panel de administración está en `http://127.0.0.1:8000/admin/`.

## Secciones

- **Inicio** (`/`): muestra un plato destacado de cada país con platos registrados. Se priorizan los platos asociados a más películas.
- **Platos** (`/platos/`, `/platos/<id>/`): catálogo y ficha de plato con descripción, país y películas asociadas.
- **Países** (`/paises/`, `/paises/<id>/`): catálogo y ficha de país con sus platos y películas.
- **Películas** (`/peliculas/`, `/peliculas/<id>/`): catálogo y ficha de película con director, sinopsis, país y platos asociados.
- **Administración** (`/admin/`): gestión de los datos mediante el panel nativo de Django.

El catálogo ampliado incluye 14 países, 65 platos y 41 películas, con relaciones navegables entre ellos.
