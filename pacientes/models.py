from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="nombre")
    apellido = models.CharField(max_length=50, verbose_name='apellido')    
    email = models.EmailField(max_length=200, blank=True)
    telefono = models.IntegerField(blank=True)
    domicilio = models.CharField(max_length=200, blank=True)
    observaciones = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)        

    class Meta:
            verbose_name='paciente'
            verbose_name_plural='pacientes'

    def __str__(self):
        return  f'{self.nombre} {self.apellido}'
