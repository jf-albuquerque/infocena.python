from django import forms

from cadastro.models import Loja,Produtos
    


class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = '__all__'

class ProdutosForm(forms.ModelForm):
    nome = forms.CharField(label="Nome do Produto " )
    preco = forms.DecimalField(label="Preço ")
    destaque = forms.BooleanField(label="Aparecer no site ?")
    class Meta:
        model = Produtos
        fields = '__all__'