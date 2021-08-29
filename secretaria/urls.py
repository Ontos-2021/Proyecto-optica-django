from django.urls import path
from . import views

urlpatterns = [
    path('listado_turnos/', views.turnos, name='listado_turnos'),
]