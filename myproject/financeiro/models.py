from django.db import models
from django.contrib.auth.models import User

class Transacao(models.Model):
    objects = None
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    usuario = models.ManyToManyField(User)
    recorrente = models.BooleanField(default=False)
    repeticoes = models.IntegerField(null=True, blank=True)

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username