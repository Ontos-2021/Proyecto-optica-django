from django.shortcuts import render, redirect
from .models import Turno
from pacientes.models import Paciente


def turnos(request):
    
    turnos = Turno.objects.all()
        
    context = {'turnos': turnos}
    return render(request, 'secretaria/homeTurnos.html', context)
"""  
def generarTurno(request):
    pacientes = Paciente.objects.all()
    
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
"""