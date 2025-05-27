from django.db import models

# Create your models here.
class MotivoContato(models.Model):
    nome = models.CharField(max_length=20)#charfield significa string


    def __str__(self):
        return f"{self.nome}"

class FaleConosco(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    MotivoContato = models.ForeignKey(MotivoContato,on_delete=models.DO_NOTHING)
    assunto = models.CharField(max_length=200)

    
    def __str__(self):
        return f"{self.nome} - {self.email} - {self.MotivoContato} - {self.assunto} "
    
class Aluquel(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    TelefoneFixo = models.CharField(max_length=20)
    TelefoneCelular = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.TelefoneFixo} - {self.TelefoneCelular}"
    
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    Telefone = models.CharField(max_length=20)

    
    def __str__(self):
        return f"{self.nome} - {self.email} - {self.Telefone}"