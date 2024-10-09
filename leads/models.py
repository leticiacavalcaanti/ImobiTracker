from django.db import models

class Lead(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=45, null=False, blank=False)
    email = models.CharField(max_length=100, null=True, blank=True)
    anotacao = models.CharField(max_length=255, null=True, blank=True)
