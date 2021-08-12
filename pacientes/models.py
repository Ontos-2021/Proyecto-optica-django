from django.db import models

# Create your models here.

class Domicilio(models.Model):

    calle = models.CharField(max_length=200)
    altura = models.IntegerField()
    barrio = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.altura} {self.barrio}'

class ObraSocial(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="nombre")
    
    class Meta:
        verbose_name='obra social'
        verbose_name_plural='obras sociales'

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="nombre")
    apellido = models.CharField(max_length=50, verbose_name='apellido')
    dni = models.IntegerField(verbose_name="Documento Nacional de Identidad", help_text="Documento Nacional de Identidad")
    email = models.EmailField(max_length=200)
    telefono = models.IntegerField()
    domicilio = models.OneToOneField(Domicilio, on_delete=models.SET_NULL, null=True)
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.SET_NULL, null=True)
    observaciones = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name='paciente'
            verbose_name_plural='pacientes'

    def __str__(self):
        return  f'Paciente {self.id}: {self.nombre} {self.apellido}'