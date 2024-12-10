from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_inicio, name='tela_inicio'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('cliente/criar/', views.cria_cliente, name='cria_cliente'),
    path('cliente/editar/<int:pk>/', views.edita_cliente, name='edita_cliente'),
    path('cliente/deletar/<int:pk>/', views.deleta_cliente, name='deleta_cliente'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),  # URL de lista de pedidos
    path('pedido/criar/', views.cria_pedido, name='cria_pedido'),
    path('pedido/editar/<int:pk>/', views.edita_pedido, name='edita_pedido'),
    path('pedido/deletar/<int:pk>/', views.deleta_pedido, name='deleta_pedido'),
]
