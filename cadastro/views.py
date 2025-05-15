from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.db.models.functions import Lower 
from cadastro.forms import LojaForm,ProdutosForm
from .models import Loja, Produtos


# Create your views here.

def index(request):
    return HttpResponse("Olá mundo! agora é web")

def listar_lojas(request):
    lojas = Loja.objects.order_by(Lower('nome'))
    return render(request, 'listar_lojas.html',
                  {'lojas':lojas})

def incluir_lojas(request ):
    if request.method == 'POST':
       form = LojaForm(request.POST)
       if form.is_valid():
           form.save()

           return listar_lojas(request)

    form = LojaForm()
    return render(request, 'incluir_lojas.html', {'formulario': form})

def alterar_loja(request, codigo):
    loja = Loja.objects.get(id=codigo)

    if request.method == 'POST' :
        form = LojaForm(request.POST, instance=loja)
        if form.is_valid():
            form.save()
            return redirect('lista_lojas')


    form = LojaForm(instance=loja)
    return render (request, 'incluir_lojas.html' , {'formulario' :form})

def excluir_loja(request, codigo):
    loja = Loja.objects.get(id=codigo)

    Loja.delete(loja)

    return redirect('lista_lojas')

def listar_produtos(request):
    produtos = Produtos.objects.order_by(Lower('nome'))
    return render(request, 'listar_produtos.html',
                  {'produtos':produtos})

def incluir_produtos(request ):
    if request.method == 'POST':
       form = ProdutosForm(request.POST)
       if form.is_valid():
           form.save()

           return listar_produtos(request)

    form = ProdutosForm()
    return render(request, 'incluir_produtos.html', {'formulario': form})

def alterar_produtos(request, codigo):
    produtos = Produtos.objects.get(id=codigo)

    if request.method == 'POST' :
        form = ProdutosForm(request.POST, instance=produtos)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')


    form = ProdutosForm(instance=produtos)
    return render (request, 'incluir_produtos.html' , {'formulario' :form})

def excluir_produtos(request, codigo):
    produtos = Produtos.objects.get(id=codigo)

    Produtos.delete(produtos)

    return redirect('listar_produtos')

def area_interna(request):
    return render(request, 'area_interna.html')