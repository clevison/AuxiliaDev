from rest_framework import serializers
from .models import Selecao

class SelecaoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Selecao
		depth = 1
		fields = ['idSelecao','idCriador','criador','idPrograma', 'nome', 'descricao', 'inicio', 'fim','vagas']