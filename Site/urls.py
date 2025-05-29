
from django.urls import path

from Site import views


urlpatterns = [
    path('',views.index, name='index'),
    path('quem_somos', views.quem_somos, name='quem_somos'),
    path('produtos', views.produtos,name='produtos'),
    path('lojas', views.lojas,name='lojas'),
    path('aluquel', views.aluquel, name='aluquel'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('fale_conosco', views.faleConosco, name='fale_conosco'),
]