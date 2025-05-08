from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),# mapeamento de rota
    path('listar_lojas', views.listar_lojas, name='lista_lojas'),
    path('incluir_lojas', views.incluir_lojas, name='incluir_lojas'),
    path('alterar_loja/<int:codigo>', views.alterar_loja, name ='alterar_loja'),
    path('excluir_loja/<int:codigo>', views.excluir_loja, name='excluir_loja'),
]

