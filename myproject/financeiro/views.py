from django.shortcuts import render
from rest_framework import generics
from .serializers import TransacaoSerializer, UserSerializer, ContaSerializer, PagamentoSerializer
from .models import Transacao, Usuario, Conta, Pagamento
import datetime
class TransacaoList(generics.ListCreateAPIView):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

class TransacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

    def perform_create(self, serializer):
        repeticoes = serializer.validated_data.get('repeticoes')
        print(repeticoes)
        recorrente = serializer.validated_data.get('recorrente')
        print(recorrente)
        if recorrente is True and repeticoes > 1:
            transacao = serializer.save()
            for i in range(repeticoes - 1):
                transacao.pk = None
                transacao.data = transacao.data + datetime.timedelta(days=30)
                transacao.save()
        else:
            print('Não processou as repetições!')
            serializer.save()

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return Usuario.objects.filter(id=self.kwargs.get('pk'))


class ContaList(generics.ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class ContaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class PagamentoList(generics.ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class PagamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

