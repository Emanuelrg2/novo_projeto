from rest_framework import serializers
from .models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        #fields = ['id', 'nome', 'email', 'endereco']
        fields = '__all__'  # Inclui todos os campos do modelo Usuarios
        read_only_fields = ['id'] # Define o campo 'id' como somente leitura
    
 