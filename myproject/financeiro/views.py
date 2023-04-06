from django.shortcuts import render
from rest_framework import generics, status
from .serializers import TransacaoSerializer, UserSerializer, ContaSerializer, PagamentoSerializer
from .models import Transacao, Usuario, Conta, Pagamento
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from dateutil.relativedelta import relativedelta

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

class TransacaoCreateAPIView(APIView):
    serializer_class = TransacaoSerializer
    def post(self, request, format=None):
        num_transacoes = request.data.get('num_transacoes', None)
        data_req = request.data.get('data', None)
        descricao_req = request.data.get('descricao', None)
        valor_req = request.data.get('valor', None)
        tipo_req = request.data.get('tipo', None)


        if not num_transacoes:
            return Response({'message': 'Por favor, forneça o número de transações.'}, status=status.HTTP_400_BAD_REQUEST)

        transacoes = []
        for i in range(num_transacoes):
            transacao = Transacao(
                data=data_req,
                descricao=descricao_req,
                valor=valor_req,
                tipo=tipo_req
            )
            transacoes.append(transacao)

        Transacao.objects.bulk_create(transacoes)

        serializer = TransacaoSerializer(transacoes, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

