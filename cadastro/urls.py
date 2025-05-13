from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),# mapeamento de rota
    path('listar_lojas', views.listar_lojas, name='lista_lojas'),
    path('incluir_lojas', views.incluir_lojas, name='incluir_lojas'),
    path('alterar_loja/<int:codigo>', views.alterar_loja, name ='alterar_loja'),
    path('excluir_loja/<int:codigo>', views.excluir_loja, name='excluir_loja'),
    path('listar_produtos',views.listar_produtos, name='listar_produtos' ),
    path('incluir_produtos', views.incluir_produtos, name='incluir_produtos'),
    path('alterar_produtos/<int:codigo>', views.alterar_produtos, name ='alterar_produtos'),
    path('excluir_produtos/<int:codigo>', views.excluir_produtos, name='excluir_produtos'),
   
]

