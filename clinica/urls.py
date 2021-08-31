"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from ventas.views import lista_pedidos, crear_pedido, modificarPedido, borrarPedido
from taller.views import vistaPedidos, cambiarEstado

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),    
    path('usuarios/', include('usuarios.urls')),
    path('usuarios/', include('django.contrib.auth.urls')),   
    #path('ventas/', include('ventas.urls')),
    #path('taller/', include('taller.urls')) ,
    path('lista_pedidos/', lista_pedidos,  name='lista_pedidos'),
    path('crear_pedido/', crear_pedido,  name='crear_pedido'),
    path('modificar_pedido/<str:pk>/', modificarPedido, name='modificar_pedido'),
    path('borrar_pedido/<str:pk>/', borrarPedido, name='borrar_pedido'),
    path('ver_pedidos/', vistaPedidos, name='ver_pedidos'),
    path('cambiar_estado/<str:pk>/', cambiarEstado, name='cambiar_estado'),

]