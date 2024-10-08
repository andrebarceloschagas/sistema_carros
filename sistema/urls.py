from django.contrib import admin  # Importa o módulo de administração do Django
from django.urls import path, include  # Importa funções para definir URLs e incluir outras configurações de URL
from sistema.views import LoginView, LogoutView  # Importa as views de login e logout do aplicativo 'sistema'
from django.views.generic import RedirectView  # Importa a view de redirecionamento do Django

urlpatterns = [
    path('admin/', admin.site.urls),  # Define a URL para a interface de administração do Django
    
    path('login/', LoginView.as_view(), name='login'),  # Define a URL para a view de login

    path('logout/', LogoutView.as_view(), name='logout'),  # Define a URL para a view de logout

    path('veiculo/', include('veiculo.urls'), name='veiculo'),  # Inclui as URLs do aplicativo 'veiculo'
    
    path('', RedirectView.as_view(url='/login/', permanent=False))  # Redireciona a raiz para a página de login

    # path('deletar/<int:id>/', DeletarVeiculo.as_view(), name='deletar_veiculo'),  # URL comentada para deletar um veículo

    # path('editar/<int:id>/', EditarVeiculo.as_view(), name='editar_veiculo'),  # URL comentada para editar um veículo

    # path('cadastrar/', CadastrarVeiculo.as_view(), name='cadastrar_veiculo'),  # URL comentada para cadastrar um veículo

    # path('listar/', ListarVeiculo.as_view(), name='listar_veiculo'),  # URL comentada para listar veículos
]