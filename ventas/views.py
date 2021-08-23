from django.shortcuts import render

from .forms import PedidoForm

# Create your views here.

def pedidos(request):
    form = PedidoForm
    context={'form': form}
    return render(request, 'ventas/form_pedidos.html', context)
