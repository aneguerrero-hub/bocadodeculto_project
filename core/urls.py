from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada, name='portada'),
    path('platos/', views.lista_platos, name='lista_platos'),
    path('platos/<int:id>/', views.detalle_plato, name='detalle_plato'),
]