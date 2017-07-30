from rest_framework import serializers
from .models import Selecao

class SelecaoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Selecao
		depth = 1
		fields = ['idSelecao','idPrograma', 'nome', 'descricao', 'inicio', 'fim']