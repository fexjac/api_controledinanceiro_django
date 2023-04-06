from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    usuario = models.ManyToManyField(User)
    num_transacoes = models.IntegerField(null=False, blank=True)
    finalizado = models.BooleanField(default=False)

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Conta(models.Model):
    banco = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    saldo_banco = models.DecimalField(max_digits=10, decimal_places=2)
    titular = models.ManyToManyField(Usuario)

class Pagamento(models.Model):
    data_pagamento = models.DateField()
    conta_usada = models.ManyToManyField(Conta)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    transacao_origem = models.ManyToManyField(Transacao)

