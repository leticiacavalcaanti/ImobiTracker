from django.db import transaction
from leads.models import Lead
from leads.serializers import LeadSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializers

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')

        # Verifica se o email já existe, se existe retorna erro 409
        if Lead.objects.filter(email=email).exists():
            return Response({"detail": "Email já existe."}, status=status.HTTP_409_CONFLICT)

        #cria um novo registro
        return super().create(request, *args, **kwargs)

