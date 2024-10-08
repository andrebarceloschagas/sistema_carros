from django.shortcuts import render, redirect  # Importa funções para renderizar templates e redirecionar URLs
from django.contrib.auth import authenticate, login, logout  # Importa funções para autenticação, login e logout de usuários
from django.views import View  # Importa a classe base para views baseadas em classe
from django.conf import settings  # Importa as configurações do projeto
from django.http import HttpResponse  # Importa a classe HttpResponse para retornar respostas HTTP

class LoginView(View):
    def get(self, request):
        # Renderiza o template de autenticação quando a requisição é GET
        return render(request, 'autenticacao.html')

    def post(self, request):
        # Obtém o nome de usuário e a senha do formulário de login
        username = request.POST['username']
        password = request.POST['password']
        
        # Autentica o usuário
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                # Faz login do usuário se ele estiver ativo
                login(request, user)
                return redirect("/veiculos")  # Redireciona para a página de veículos (comentado)
            # Renderiza o template de autenticação com mensagem de usuário inativo
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo!'})

        # Renderiza o template de autenticação com mensagem de login ou senha inválidos
        return render(request, 'autenticacao.html', {'mensagem': 'Login ou senha inválido!'})

class LogoutView(View):
    def get(self, request):
        # Faz logout do usuário
        logout(request)
        # Redireciona para a URL de login definida nas configurações
        return redirect(settings.LOGIN_URL)