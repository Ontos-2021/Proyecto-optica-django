from django.forms import ModelForm
from .models import Turno
from pacientes.models import Paciente

class TurnoForm(ModelForm):

    class Meta:
        model = Turno
        fields = '__all__'

class PacienteForm(ModelForm):
    
    class Meta:
        model = Paciente
        fields = '__all__'
