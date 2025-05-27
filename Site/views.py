from django.shortcuts import render

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

def FaleConosco(request):
    form = fale_ConoscoForm()
    return = render(resquest,'fale_conosco.html',)