from django.contrib import admin
from . models import Producto

@admin.register(Producto)
class Admin(admin.ModelAdmin):
    '''Admin View for Producto'''

    list_display = ['nombre', 'precio', 'stock']
    list_filter = ['nombre', 'categoria', 'precio']   
    readonly_fields = ['created', 'updated']
    search_fields = ['nombre', 'categoria']   
   
