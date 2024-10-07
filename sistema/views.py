from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.conf import settings
from django.http import HttpResponse

class LoginView(View):
    def get(self, request):
        return render(request, 'autenticacao.html')


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Login efetuado com sucesso!')
                # return redirect("/veiculos")
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo!'})

        return render(request, 'autenticacao.html', {'mensagem': 'Login ou senha inválido!'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)