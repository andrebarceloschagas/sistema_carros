from django.shortcuts import render
from django.views.generic import ListView
from .models import Veiculo

class ListarVeiculos(ListView):
    model = Veiculo
    template_name = 'veiculo/listar.html'
    context_object_name = 'veiculos'