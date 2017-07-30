from .serializer import ProgramaSerializer
from .models import Programa 

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import render
from django.http import Http404


# Create your views here.
def lista_programas(request):
    programas = Programa.objects.all()
    context = {'programas': programas}
    return render(request, 'programa/lista_programas.html', context)


class ProgramaListView(APIView):
    serializer_class = ProgramaSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Programa.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class ProgramaView(APIView):

    def get(self, request, pk, format=None):
        user = Programa.objects.get(pk=pk)
        serializer = ProgramaSerializer(user)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Programa.objects.get(pk=pk)
        except Programa.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        programa = self.get_object(pk)
        serializer = ProgramaSerializer(programa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print("Estou no delete")
        programa = self.get_object(pk)
        programa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    