from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),# mapeamento de rota
   
]

