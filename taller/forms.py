from django.forms import ModelForm
from ventas.models import Pedido

class PedidoForm(ModelForm):

    class Meta:
        model = Pedido
        fields = '__all__'

