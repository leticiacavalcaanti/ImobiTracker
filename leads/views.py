from leads.models import Lead
from leads.serializers import LeadSerializers
from rest_framework import viewsets

class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializers

