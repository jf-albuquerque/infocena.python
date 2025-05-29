from django.shortcuts import render
from Site.forms import Aluquelform, Clienteform, FaleConoscoform

from cadastro.models import Loja, Produtos
from django.db.models.functions import Lower

# Create your views here.
def index(request):
    return render(request,'index.html')

def quem_somos(request):
    return render(request, 'quem_somos.html')

def produtos(request):
    produtos = Produtos.objects.order_by(Lower('nome'))
    return render(request, 'produtos.html', {'produtos': produtos})

def lojas(request):
    lojas = Loja.objects.order_by(Lower('nome'))
    return render(request, 'lojas.html', {'lojas': lojas})

def faleConosco(request):
    if request.method == 'POST':
       form = FaleConoscoform(request.POST)
       if form.is_valid():
           form.save()

           return index(request)
    form = FaleConoscoform()
    return render(request, 'fale_conosco.html', {'formulario': form})

def aluquel(request):
    if request.method == 'POST':
       form = Aluquelform(request.POST)
       if form.is_valid():
           form.save()
           return index(request)
    form = Aluquelform()
    return render(request, 'aluquel.html', {'formulario': form})
       
def cadastro(request):
    if request.method == 'POST':
       form = Clienteform(request.POST)
       if form.is_valid():
           form.save()
           return index(request)
       
    form = Clienteform()
    return render(request, 'cadastro.html', {'formulario': form})
    
    