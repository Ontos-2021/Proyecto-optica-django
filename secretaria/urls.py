from django.urls import path
from . import views

urlpatterns = [
    path('listado_turnos/', views.turnos, name='listado_turnos'),
    path('nuevo_turno/', views.nuevoTurno, name='nuevo_turno'),
    path('modificar_turno/<str:pk>', views.modificarTurno, name='modificar_turno'),
    path('borrar_turno/<str:pk>', views.borrarTurno, name='borrar_turno'),
    path('ver_paciente/<str:pk>', views.verPaciente, name='ver_paciente'),
    path('nuevo_paciente/', views.nuevoPaciente, name='nuevo_paciente'),
    path('borrar_paciente/<str:pk>', views.borrarPaciente, name='borrar_paciente'),
]