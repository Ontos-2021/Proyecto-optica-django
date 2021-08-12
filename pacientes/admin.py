from django.contrib import admin
from pacientes.models import Paciente, Domicilio, ObraSocial
# Register your models here.

@admin.register(Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    '''Admin View for Paciente'''

    list_display = ['id', 'calle', 'altura', 'barrio', 'ciudad', 'provincia']
    list_filter = ['provincia']
    search_fields = ['barrio', 'ciudad']

@admin.register(ObraSocial)
class ObraSocialAdmin(admin.ModelAdmin):
    '''Admin View for ObraSocial'''

    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    '''Admin View for Paciente'''

    list_display = ['nombre', 'apellido']