from rest_framework import serializers
from .models import Transacao
from django.contrib.auth.models import User

class TransacaoSerializer(serializers.ModelSerializer):
    tipo = serializers.ChoiceField(choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    usuario = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    recorrente = serializers.BooleanField()
    repeticoes = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Transacao
        fields = ('id', 'data', 'descricao', 'valor', 'tipo', 'usuario', 'recorrente', 'repeticoes')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')