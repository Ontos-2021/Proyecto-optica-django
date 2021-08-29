from django.db import models
from pacientes.models import Paciente
from usuarios.models import Usuario


class Turno(models.Model):
   
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)    
    fecha = models.DateTimeField(null=True)
    doctor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)  
    asistencia = models.BooleanField(default=False)
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
    
    def __str__(self):
        return f'{self.paciente.nombre} {self.fecha}'