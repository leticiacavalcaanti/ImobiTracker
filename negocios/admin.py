from django.contrib import admin
from negocios.models import Negocio

class NegocioAdmin(admin.ModelAdmin):
    list_display = ('id','descricao','lead','usuario','dataInclusao','previsaoVenda','vencimentoAtualizacao','dataFechamento','etapa')
    list_display_links = ('id','descricao',)
    list_per_page = 15
    search_fields = ('descricao',)

admin.site.register(Negocio, NegocioAdmin)

''' descricao = models.TextField(null=False, blank=False)
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    dataInclusao= models.DateTimeField(auto_now_add=True)
    previsaoVenda = models.DateField(null=False, blank=False)
    vencimentoAtualizacao = models.DateField(null=False, blank=False)
    dataFechamento = models.DateField(null=True, blank=True)
    etapa = models.CharField(max_length=45, null=False, blank=False)
'''
