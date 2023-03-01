from django.urls import path
from .views import TransacaoList, UserList
from . import views

urlpatterns = [
    path('usuarios/', views.UserList.as_view(), name='user-list'),
    path('usuarios/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('transacoes/', views.TransacaoList.as_view(), name='transacao-list'),
    path('transacoes/<int:pk>/', views.TransacaoDetail.as_view(), name='transacao-detail'),
]