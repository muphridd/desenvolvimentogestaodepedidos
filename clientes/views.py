from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Pedido
from .forms import ClienteForm, PedidoForm

def tela_inicio(request):
    return render(request, 'clientes/tela_inicio.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def cria_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cria_cliente.html', {'form': form})

def edita_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/edita_cliente.html', {'form': form})

def deleta_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/deleta_cliente.html', {'cliente': cliente})

def cria_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')  # Certifique-se de que a URL 'lista_pedidos' esteja definida
    else:
        form = PedidoForm()
    return render(request, 'clientes/cria_pedido.html', {'form': form})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'clientes/lista_pedidos.html', {'pedidos': pedidos})

def edita_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'clientes/edita_pedido.html', {'form': form})

def deleta_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'clientes/deleta_pedido.html', {'pedido': pedido})
