from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView



urlpatterns = [
    
   
    path('aeropuertos/', aeropuertos, name="aeropuertos"),
    path('trips/', trips, name="trips"),
    path('eliminarAeropuerto/<id>', eliminarAeropuerto, name="eliminarAeropuerto"),
    path('editarAeropuerto/<id>', editarAeropuerto, name="editarAeropuerto"),
    path('trip/list/', TripList.as_view(), name="trip_list"),
    path('trip/nuevo/', TripCreacion.as_view(), name="trip_crear"),
    path('trip/<pk>', TripDetalle.as_view(), name="trip_detalle"),
    path('trip/borrar/<pk>', TripDelete.as_view(), name="trip_borrar"),
    path('trip/editar/<pk>', TripUpdate.as_view(), name="trip_editar"),
    
]