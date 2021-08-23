from django.contrib import admin
from . models import Producto, Pedido

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    '''Admin View for Producto'''

    list_display = ['nombre', 'precio', 'stock']
    list_filter = ['nombre', 'categoria', 'precio']   
    readonly_fields = ['created', 'updated']
    search_fields = ['nombre', 'categoria']   
   
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    '''Admin View for Pedido'''

    list_display = ['fecha_pedido', 'paciente', 'estado' ]
    list_filter = ['vendedor', 'paciente', 'producto', 'estado', 'fecha_pedido']   
    readonly_fields = ['fecha_pedido']
    search_fields = ['vendedor', 'paciente', 'producto', 'estado', 'fecha_pedido']   
   