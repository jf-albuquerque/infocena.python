from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),# mapeamento de rota
    path('listar_lojas', views.listar_lojas, name='lista_lojas'),
    path('incluir_lojas', views.incluir_lojas, name='incluir_lojas'),
]

