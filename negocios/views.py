
from negocios.models import Negocio
from negocios.serializers import NegocioSerializers
from rest_framework import viewsets

class NegociosViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializers


