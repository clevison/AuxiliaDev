from django.contrib.auth.models import User, Group
from rest_framework import serializers


# class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(usuarioView="usuario:user-detail")
#     class Meta:
#         model = User
#         fields = ('url', 'username')


# class GrupoSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')