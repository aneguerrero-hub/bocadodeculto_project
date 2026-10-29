# Bocado de Culto

Proyecto web colaborativo en Django para explorar la relación entre platos, países y películas.

## Requisitos

- Python 3.10 o superior compatible con la versión de Django instalada.
- Django (la versión utilizada en el entorno de desarrollo del proyecto es 6.1.2).

## Puesta en marcha

Desde la carpeta que contiene `manage.py`:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS / Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
# Solo si la base de datos está vacía y quieres cargar los datos de ejemplo:
python manage.py loaddata core/fixtures/demo_data.json
python manage.py runserver
```

Después, abre `http://127.0.0.1:8000/`. El panel de administración está en `http://127.0.0.1:8000/admin/`.

## Secciones

- **Inicio** (`/`): muestra un plato destacado de cada país con platos registrados. Se priorizan los platos asociados a más películas.
- **Platos** (`/platos/`, `/platos/<id>/`): catálogo y ficha de plato con descripción, precio, país y películas asociadas.
- **Países** (`/paises/`, `/paises/<id>/`): catálogo y ficha de país con sus platos y películas.
- **Películas** (`/peliculas/`, `/peliculas/<id>/`): catálogo y ficha de película con director, sinopsis, país y platos asociados.
- **Administración** (`/admin/`): gestión de los datos mediante el panel nativo de Django.

Los datos de ejemplo se incluyen en `core/fixtures/demo_data.json` para poder reconstruir el catálogo en una base de datos nueva. La base de datos SQLite incluida en este paquete ya contiene esos datos, así que no cargues la fixture encima de ella.

Los estilos compartidos están en `static/css/base.css`; cada sección amplía esos estilos desde su propia hoja CSS. Las plantillas usan las variables de contexto proporcionadas por `core/views.py` y enlaces nombrados de `core/urls.py`.
