from django.db import models

class Usuario(models.Model):
    nivelDeAcesso = models.CharField(max_length=100)
    nome = models.CharField(max_length=255, null=False, blank=False)
    login = models.CharField(max_length=100, unique=True, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)
    creci = models.CharField(max_length=100, unique=True)
    cargo = models.CharField(max_length=100, null=False, blank=False)

