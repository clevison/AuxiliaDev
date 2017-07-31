from rest_framework import serializers

from .models import Selecao, Participe

class SelecaoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Selecao
		depth = 1
		fields = ['idSelecao','idCriador','criador','idPrograma', 'nome', 'descricao', 'inicio', 'fim','vagas','participantes']


class ParticipeSelecaoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Selecao
		depth = 1
		fields = ['idSelecao','participantes']

class ParticipeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Participe
		depth = 1
		fields = ['idUsuario','nome']
		# fields = ['idParticipe','idSelecao','idUsuario']