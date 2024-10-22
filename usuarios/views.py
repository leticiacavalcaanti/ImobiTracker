from django.db import transaction
from rest_framework import viewsets
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializers
from rest_framework.response import Response
from rest_framework import status

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        login = request.data.get('login')

        # Verifica se o login já existe, se existe retorna erro 409
        if Usuario.objects.filter(login=login).exists():
            return Response({"detail": "login já existe."}, status=status.HTTP_409_CONFLICT)

        #cria um novo registro
        return super().create(request, *args, **kwargs)
