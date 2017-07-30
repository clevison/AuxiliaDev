from django.db import models

# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from usuario.serializer import UsuarioSerializer
# from rest_framework import viewsets
# from rest_framework.response import Response

# class UsuarioViewSet(viewsets.ViewSet):
	
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UsuarioSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UsuarioSerializer(user)
#         return Response(serializer.data)