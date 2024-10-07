from django.db import models
from django.urls import path
from veiculo.views import ListarVeiculos

urlpatterns = [
    path('listar/', ListarVeiculos.as_view(), name='listar_veiculos'),
]
