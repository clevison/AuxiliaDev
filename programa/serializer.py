from rest_framework import serializers
from .models import Programa

class ProgramaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Programa
		depth = 1
		fields = ['id_programa','id_criador','criador', 'titulo', 'descricao']