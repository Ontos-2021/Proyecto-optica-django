from django.shortcuts import render, redirect
from ventas.models import Pedido, Producto
from usuarios.models import Usuario
from .forms import PedidoForm

# Create your views here.

def vistaPedidos(request):
    pedidos = Pedido.objects.all()    
    usuarios = Usuario.objects.all()
    productos = Producto.objects.all()
    en_taller = pedidos.filter(estado='taller').count()
    finalizado = pedidos.filter(estado='finalizado').count()
        
    context = {'pedidos': pedidos,             
               'usuarios': usuarios,
               'productos': productos,            
               'en_taller': en_taller, 
               'finalizado': finalizado,               
              }
    return render(request, 'taller/ver_pedidos.html', context)
    
def cambiarEstado(request, pk):
    pedido = Pedido.objects.get(id=pk)
    form = PedidoForm(instance=pedido)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
        return redirect('/lista_pedidos/')
    context = {'form': form}
    return render(request, 'taller/cambiar_estado.html', context )  
