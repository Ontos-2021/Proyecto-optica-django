from django.urls import path
from . import views

urlpatterns = [
    path('listado_turnos/', views.turnos, name='listado_turnos'),
    path('nuevo_turno/', views.nuevoTurno, name='nuevo_turno'),
    path('modificar_turno/<str:pk>', views.modificarTurno, name='modificar_turno'),
    path('borrar_turno/<str:pk>', views.borrarTurno, name='borrar_turno'),
]