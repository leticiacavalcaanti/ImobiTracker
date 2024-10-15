from django.db import models
from usuarios.models import Usuario
from leads.models import Lead


class Negocio(models.Model):
    descricao = models.TextField(null=False, blank=False)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dataInclusao= models.DateTimeField(auto_now_add=True)
    previsaoVenda = models.DateField(null=False, blank=False)
    vencimentoAtualizacao = models.DateField(null=False, blank=False)
    dataFechamento = models.DateField(null=True, blank=True)
    etapa = models.CharField(max_length=45, null=False, blank=False)



