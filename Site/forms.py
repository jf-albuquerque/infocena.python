from django import forms
from Site.models import Aluquel, Cliente, FaleConosco

from cadastro.models import Loja  



class FaleConoscoform(forms.ModelForm):
   nome = forms.CharField(label="Nome do cliente " )
   email = forms.EmailField(label="Email ")
   Telefone = forms.CharField(label="Tefone: ")
   assunto = forms.CharField(label="")
   class Meta:
        model = FaleConosco
        fields = '__all__'
       # labels = {
            
     #   }

class Aluquelform(forms.ModelForm):
   nome = forms.CharField(label="Nome do cliente " )
   email = forms.EmailField(label="Email ")
   TelefoneFixo = forms.CharField(label="Tefone fixo: ")
   TelefoneCelular = forms.CharField(label="Tefone celular: ")
   class Meta:
        model = Aluquel
        fields = '__all__'
    


class Clienteform(forms.ModelForm):
   nome = forms.CharField(label="Nome do cliente " )
   cpf = forms.CharField(label="informe cpf: ")
   email = forms.EmailField(label="Email ")
   Telefone = forms.CharField(label="Tefone: ")
   class Meta:
        model = Cliente
        fields = '__all__'
    
