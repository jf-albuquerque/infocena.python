from django import forms

from cadastro.models import Loja  



class FaleConosco(forms.modelForm):
   nome = forms.CharField(label="Nome do cliente " )
   email = forms.EmailField(label="Email ")
   Telefone = forms.CharField(label="Tefone: ")
   assunto = forms.CharField(label="")

class Aluquel(forms.modelForm):
   nome = forms.CharField(label="Nome do cliente " )
   email = forms.EmailField(label="Email ")
   TelefoneFixo = forms.CharField(label="Tefone fixo: ")
   TelefoneCelular = forms.CharField(label="Tefone celular: ")

class Cliente(forms.modelForm):
   nome = forms.CharField(label="Nome do cliente " )
   cpf = forms.CharField(label="informe cpf: ")
   email = forms.EmailField(label="Email ")
   Telefone = forms.CharField(label="Tefone: ")