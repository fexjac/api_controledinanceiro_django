from django.urls import path
from .views import TransacaoList, UserList

urlpatterns = [
    path('transacoes/', TransacaoList.as_view(), name='transacao-list'),
    path('usuarios/', UserList.as_view(), name='usuario-list'),
]
