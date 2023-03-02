from django.shortcuts import render
from rest_framework import generics
from .serializers import TransacaoSerializer, UserSerializer
from .models import Transacao, User
import datetime
class TransacaoList(generics.ListCreateAPIView):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

class TransacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        repeticoes = serializer.validated_data.get('repeticoes')
        recorrente = serializer.validated_data.get('recorrente')
        if recorrente and repeticoes is not None and repeticoes > 1:
            transacao = serializer.save()
            for i in range(repeticoes - 1):
                transacao.pk = None
                transacao.data = transacao.data + datetime.timedelta(days=7)
                transacao.save()
        else:
            serializer.save()