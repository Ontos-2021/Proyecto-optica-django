from django.contrib import admin
from pacientes.models import Paciente
# Register your models here.

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    '''Admin View for Paciente'''

    list_display = ['nombre']