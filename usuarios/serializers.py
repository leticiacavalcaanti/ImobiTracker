from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioSerializers(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Usuario
        fields = ['id','nivelDeAcesso','nome','login','senha','creci','cargo']
