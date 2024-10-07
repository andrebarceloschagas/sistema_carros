from django.contrib import admin
from django.urls import path, include
from sistema.views import LoginView, LogoutView
from sistema import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),

    path('veiculo/', include('veiculo.urls'), name='veiculo')

    # path('deletar/<int:id>/', DeletarVeiculo.as_view(), name='deletar_veiculo')


]
