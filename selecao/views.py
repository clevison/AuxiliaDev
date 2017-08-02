from django.shortcuts import render

from .serializer import SelecaoSerializer, ParticipeSerializer, ParticipeSelecaoSerializer
from .models import Selecao, Participe

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import render
from django.http import Http404


# Create your views here.
class SelecaoListView(APIView):
    serializer_class = SelecaoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Selecao.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class SelecaoView(APIView):

    def get(self, request, pk, format=None):
        selecao = Selecao.objects.get(pk=pk)
        serializer = SelecaoSerializer(selecao)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Selecao.objects.get(pk=pk)
        except Selecao.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        selecao = self.get_object(pk)
        serializer = SelecaoSerializer(selecao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        selecao = self.get_object(pk)
        selecao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ParticipantesView(APIView):
    serializer_class = ParticipeSerializer

    def get(self, request, pk, format=None):
        selecao = Selecao.objects.filter(idSelecao=pk)
        serializer = ParticipeSelecaoSerializer(selecao, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        selecao = Selecao.objects.get(idSelecao=pk)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # print(serializer)
            serializer.save()
            participante = Participe.objects.get(idUsuario=serializer.data["idUsuario"])
            # selecao.participantes.add(serializer.data["idUsuario"])
            selecao.participantes.add(participante)
            selecao.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

            # print(serializer.data["idUsuario"])
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

    def delete(self, request, pk, format=None):
        selecao = Selecao.objects.get(idSelecao=pk)

        participe = self.serializer_class(data=request.data)

        if participe.is_valid():
            idUsuario = participe.data["idUsuario"]
            print(idUsuario)
            selecao.participantes.remove(idUsuario)
            selecao.save()
        

            return Response(status=status.HTTP_204_NO_CONTENT)
        # participe = self.serializer_class(data=request.data)
        # idUsuario = participe.data["idUsuario"]
        # idUsuario =  self.request.query_params.get('idUsuario', None)
        # print(idUsuario)
      

class ParticipeListView(APIView):
    serializer_class = ParticipeSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Participe.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class ParticipeView(APIView):

    def get(self, request, pk, format=None):
        selecao = Selecao.objects.filter(idSelecao=pk)
        serializer = ParticipeSelecaoSerializer(selecao, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        selecao = Selecao.objects.get(isSelecao = pk)
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # print(serializer)
            serializer.save()
            # selecao.save(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

    def delete(self, request, pk, format=None):
        idUsuario =  self.request.query_params.get('idUsuario', None)
        participe = Participe.objects.get(idSelecao=pk, idUsuario=idUsuario)
        participe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)