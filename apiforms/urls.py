from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import busqueda, CrearBusqueda,Resultados, EliminarBusqueda, EditarBusqueda


urlpatterns = [
    path('busqueda/', login_required(busqueda.as_view()), name= 'Busquedas'),
    path('busqueda/crear_busqueda/', login_required(CrearBusqueda.as_view()), name='crear_busqueda'),
    path('resultados/', login_required(Resultados.as_view()), name= 'resultados'),
    path('busqueda/editar_busqueda/<int:pk>', login_required(EditarBusqueda.as_view()), name = 'editar_busqueda'),
    path('busqueda/eliminar_busqueda/<int:pk>', login_required(EliminarBusqueda.as_view()), name = 'eliminar_busqueda'),
]