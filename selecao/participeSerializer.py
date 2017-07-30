from rest_framework import serializers
from .models import Participe

class ParticipeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Participe
		depth = 1
		fields = ['idParticipe','idSelecao','idUsuario']