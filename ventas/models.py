from django.db import models
from django.db.models.fields import DateTimeField
from pacientes.models import Paciente
from usuarios.models import Usuario

class Producto(models.Model):

    CATEGORIAS = [
    ('lente', 'lente'),
    ('otra', 'otra'),    
    ]
    
    nombre = models.CharField(max_length=50)    
    categoria = models.CharField(choices=CATEGORIAS, max_length=10)
    precio = models.FloatField()    
    stock = models.IntegerField(default=1, null=True)     
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)  

    class Meta:

        verbose_name= "producto"
        verbose_name_plural="productos"    

    def __str__(self):
        return f'{self.nombre} '

class Pedido(models.Model):

    ESTADO = (
        ('pendiente', 'pendiente'),
        ('pedido','pedido'),
        ('taller', 'taller'),
        ('finalizado', 'finalizado'),
    )
    paciente = models.ForeignKey(Paciente, null=True, on_delete=models.SET_NULL)
    
    vendedor = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(Producto, null=True, on_delete=models.SET_NULL)
    cantidad = models.IntegerField(default=1)
    fecha_pedido= models.DateTimeField(auto_now_add=True,  null=True) 
    estado = models.CharField(max_length=200, null=True, choices=ESTADO)
    
    def subtotal(self):
        return f'{self.producto.precio} * {self.cantidad}' 

    def total(self):
        return sum({self.producto.precio*self.cantidad})    

    def __str__(self):
        return self.producto.nombre