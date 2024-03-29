from django.urls import path
from .views import TransacaoList, UsuarioList, ContaList, PagamentoList, TransacaoCreateAPIView
from . import views

urlpatterns = [
    path('usuarios/', views.UsuarioList.as_view(), name='user-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view(), name='user-detail'),
    path('transacoes/', views.TransacaoList.as_view(), name='transacao-list'),
    path('transacoes/<int:pk>/', views.TransacaoDetail.as_view(), name='transacao-detail'),
    path('transacoes/teste/', views.TransacaoCreateAPIView.as_view(), name='transacao-detalhe'),
    path('contas/', views.ContaList.as_view(), name='contas-list'),
    path('contas/<int:pk>/', views.ContaDetail.as_view(), name='conta-detail'),
    path('pagamentos/', views.PagamentoList.as_view(), name='pagamentos-list'),
    path('pagamentos/<int:pk>/', views.PagamentoDetail.as_view(), name='pagamento-detail'),
]