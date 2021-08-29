# ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
   path('lista_pedidos/', views.lista_pedidos,  name='lista_pedidos'),
   path('crear_pedido/', views.crear_pedido,  name='crear_pedido'),
   path('modificar_pedido/<str:pk>/', views.modificarPedido, name='modificar_pedido'),
   path('borrar_pedido/<str:pk>/', views.borrarPedido, name='borrar_pedido'),
]

