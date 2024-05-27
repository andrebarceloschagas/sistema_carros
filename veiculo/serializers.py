from rest_framework import serializers
from veiculo.models import Veiculo

class SerializadorVeiculo(serializers.ModelSerializer):
    '''
    Classe SerializadorVeiculo
    '''
    class Meta:
        '''
        Classe Meta
        '''
        model = Veiculo
        exclude = []


