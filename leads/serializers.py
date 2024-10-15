from rest_framework import serializers
from leads.models import Lead

class LeadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id','nome','telefone','email','anotacao']