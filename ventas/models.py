from django.db import models
from django.db.models.fields import DateTimeField
from usuarios.models import Usuario
from pacientes.models import Paciente 


class Categorias(models.TextChoices):
    LENTES = 'Lentes'
    ARMAZONES = 'Armazones'
    ACCESORIOS = 'Accesorios'
    ORTOPTICA = 'Ortóptica'
    OTRAS = 'Otras'

class Producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    detalles = models.TextField(blank=True, null=True)
    categoria = models.CharField(choices=Categorias.choices, max_length=10)
    precio = models.FloatField()    
    stock = models.IntegerField(default=1, null=True)
    imagen = models.ImageField(upload_to='ventas', null=True, blank=True) 
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)  

    class Meta:

        verbose_name= "producto"
        verbose_name_plural="productos"    

    def __str__(self):
        return self.nombre
   
class Pedido(models.Model):
    
    ESTADOS = (
    ('pendiente', 'pendiente'),
    ('pedido', 'pedido'),
    ('taller', 'taller'),
    ('finalizado', 'finalizado'),
    )

    FORMAS_PAGO = (
        ('credito', 'credito'),        
        ('debito', 'debito'),
        ('billetera_virtual', 'billetera_virtual'),
        ('efectivo', 'efectivo'),
    )

    vendedor = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)  
    producto = models.ManyToManyField(Producto) 
    cantidad = models.IntegerField()       
    forma_pago = models.CharField(max_length=20, default='credito', choices=FORMAS_PAGO, verbose_name='Forma de pago')    
    estado = models.CharField(choices=ESTADOS, default='pendiente', max_length=10)
    fecha_pedido = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateField(auto_now = True, verbose_name="Fecha cambio de estado", null=True)

    def subtotal(self):      
        return ({self.producto.precio} * {self.cantidad})
    def total(self):      
        return sum({self.producto.precio} * {self.cantidad})    
       
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return (f'Pedido de {self.paciente.nombre}')
        