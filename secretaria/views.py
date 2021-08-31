from django.shortcuts import render, redirect
from .models import Turno
from .forms import TurnoForm, PacienteForm
from pacientes.models import Paciente


def verPaciente(request, pk):
    paciente = Paciente.objects.get(id=pk)
    form = PacienteForm(instance=paciente)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
        return redirect('/listado_turnos/')
    context = {'form': form}
    return render(request, 'secretaria/ver_paciente.html', context )  

def nuevoPaciente(request):
    form = PacienteForm
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('listado_turnos')
       
    context={'form': form}
    return render(request, 'secretaria/nuevo_paciente.html', context)


def borrarPaciente(request, pk):
    paciente = Paciente.objects.get(id=pk)
    if request.method == "POST":
        paciente.delete() 
        return redirect('listado_turnos')
    context = {'paciente': paciente}
    return render(request, 'secretaria/borrar_paciente.html', context)    


def turnos(request):
    pacientes = Paciente.objects.all()
    turnos = Turno.objects.all()
        
    context = {'turnos': turnos, 'pacientes': pacientes}
    return render(request, 'secretaria/homeTurnos.html', context)

def nuevoTurno(request):
    turnos = Turno.objects.all()    
    form = TurnoForm
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('listado_turnos')
       
    context={'form': form, 'turnos': turnos}
    return render(request, 'secretaria/nuevoTurno.html', context)

def modificarTurno(request, pk):
    turno = Turno.objects.get(id=pk)
    form = TurnoForm(instance=turnos)
    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
        return redirect('/listado_turnos/')
    context = {'form': form}
    return render(request, 'secretaria/modificarTurno.html', context )  


def borrarTurno(request, pk):
    turno = Turno.objects.get(id=pk)
    if request.method == "POST":
        turno.delete() 
        return redirect('listado_turnos')
    context = {'turno': turno}
    return render(request, 'secretaria/borrar_turno.html', context)    
