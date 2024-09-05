from django.contrib import admin
from django.urls import path, include
from sistema.views import Login, Logout
from sistema import views

urlpatterns = [
    # path('logout/', Logout.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name = 'index'),
    # path('veiculo/', include('veiculo.urls'), name='veiculo')
    # path('deletar/<int:id>/', DeletarVeiculo.as_view(), name='deletar_veiculo')
]
