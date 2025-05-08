from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.db.models.functions import Lower 
from cadastro.forms import LojaForm
from .models import Loja
from .models import Loja


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