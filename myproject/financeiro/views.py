from rest_framework import generics
from django.contrib.auth.models import User
from .models import Transacao
from .serializers import TransacaoSerializer, UserSerializer

class TransacaoList(generics.ListCreateAPIView):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

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

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer