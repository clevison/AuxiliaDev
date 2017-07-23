from .serializer import ProgramaSerializer
from .models import Programa 

from rest_framework import Response
from rest_framework import APIView
from rest_framework import status
from django.shortcuts import render


# Create your views here.
def lista_programas(request):
	programas = Programas.objects.all()
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
