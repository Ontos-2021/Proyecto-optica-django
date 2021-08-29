from django.forms import ModelForm
from .models import Turno

class TurnoForm(ModelForm):

    class Meta:
        model = Turno
        fields = '__all__'
