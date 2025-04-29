from django.db import models

# Create your models here.
class Loja(models.Model):
    nome = models.CharField(max_length=100)#charfield significa string
    telefone = models.CharField(max_length=20)

 