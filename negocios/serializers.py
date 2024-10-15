from rest_framework import serializers
from negocios.models import Negocio

class NegocioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = ['id','descricao','lead','usuario','dataInclusao','previsaoVenda','vencimentoAtualizacao','dataFechamento','etapa']