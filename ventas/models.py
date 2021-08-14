from django.db import models
from django.db.models.fields import DateTimeField

class Producto(models.Model):
    
    Categorias = models.TextChoices('Categoria', 'Lentes Armazones Accesorios Ortóptica Otras')
    nombre = models.CharField(max_length=50)
    detalles = models.TextField(blank=True, null=True)
    categoria = models.CharField(blank=True, choices=Categorias.choices, max_length=10)
    precio = models.FloatField()    
    stock = models.IntegerField(default=1, null=True)
    imagen = models.ImageField(upload_to='ventas', null=True, blank=True) 
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)  

    class Meta:

        verbose_name= "producto"
        verbose_name_plural="productos"    

    def __str__(self):
        return f'{self.nombre} '

