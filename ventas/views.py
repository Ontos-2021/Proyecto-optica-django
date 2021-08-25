from django.shortcuts import render, redirect
from .models import Pedido, Producto
from pacientes.models import Paciente
from usuarios.models import Usuario
from .forms import PedidoForm

# Create your views here.

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    pacientes = Paciente.objects.all()
    usuarios = Usuario.objects.all()
    productos = Producto.objects.all()
    pedidos_totales= pedidos.count()
    pendientes = pedidos.filter(estado='pendiente').count()
    est_pedidos = pedidos.filter(estado='pedido').count()
    en_taller = pedidos.filter(estado='taller').count()
    finalizado = pedidos.filter(estado='finalizado').count()
        
    context = {'pedidos': pedidos,
              'pacientes': pacientes, 
              'usuarios': usuarios,
              'productos': productos,
              'pedidos_totales': pedidos_totales,
               'pendientes': pendientes, 
               'est_pedidos': est_pedidos,
               'en_taller': en_taller, 
                'finalizado': finalizado,
               
                 }
    return render(request, 'ventas/lista_pedidos.html', context)
    
def  crear_pedido(request):
    usuarios = Usuario.objects.all()
    form = PedidoForm
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('lista_pedidos')
    context={'form': form, 'usuarios': usuarios}
    return render(request, 'ventas/nuevo_pedido.html', context)

def modificarPedido(request, pk):
    pedido = Pedido.objects.get(id=pk)
    form = PedidoForm(instance=pedido)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    context = {'form': form}
    return render(request, 'ventas/nuevo_pedido.html', context )  

def borrarPedido(request, pk):
    pedido = Pedido.objects.get(id=pk)
    if request.method == "POST":
        pedido.delete() 
        return redirect('lista_pedidos')
    context = {'pedido': pedido}
    return render(request, 'ventas/borrar_pedido.html', context)    
