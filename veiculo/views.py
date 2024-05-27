from django.shortcuts import render
from django.views.generic import View
from veiculo.models import Veiculo

class ListarVeiculos(Lo):
    '''
    View para listar veículos cadastrados
    '''

    
):
    

class CadastrarVeiculo(View):
    '''
    View para cadastrar um veículo
    '''
    def get(self, request):
        return render(request, 'veiculo/cadastrar.html')
    
    def post(self, request):
        dados = request.POST
        veiculo = Veiculo(
            marca=dados['marca'],
            modelo=dados['modelo'],
            ano=dados['ano'],
            preco=dados['preco']
        )
        veiculo.save()
        return render(request, 'veiculo/cadastrar.html', {'mensagem': 'Veículo cadastrado com sucesso!'})
    

class DetalharVeiculo(View):
    '''
    View para detalhar um veículo
    '''
    def get(self, request, id):
        veiculo = Veiculo.objects.get(id=id)
        contexto = {
            'veiculo': veiculo
        }
        return render(request, 'veiculo/detalhar.html', contexto)
    
class DeletarVeiculo(View):
    '''
    View para deletar um veículo
    '''
    model = Veiculo
    template_name = 'veiculo/deletar.html'
    
    def get(self, request, id):
        veiculo = Veiculo.objects.get(id=id)
        veiculo.delete()
        return render(request, 'veiculo/deletar.html', {'mensagem': 'Veículo deletado com sucesso!'})
    
    class APIListarVeiculo(ListarAPIView):
        serializer_class = SerializadorVeiculo

        def get_queryset(self):
            return Veiculo.objects.all()
