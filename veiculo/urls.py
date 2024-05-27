from django.urls import path
from django.contrib import admin
from veiculo.views import ListarVeiculos


urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar_veiculos'),
    path('api/', APIListarVeiculos.as_view(), name='api_listar_veiculos'),
    
]
