from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(models.Model):
    nivelDeAcesso = models.CharField(max_length=100)
    nome = models.CharField(max_length=255, null=False, blank=False)
    login = models.CharField(max_length=100, unique=True, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)
    creci = models.CharField(max_length=100, unique=True, null=True)
    cargo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome