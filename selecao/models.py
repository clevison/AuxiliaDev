from programa.models import Programa

from django.db import models


# Create your models here.
class Selecao(models.Model):
	idSelecao = models.AutoField(primary_key=True)
	idPrograma = models.IntegerField(verbose_name = 'Id do programa')
	# idPrograma = models.ForeignKey('programa.Programa', on_delete=models.CASCADE)
	nome = models.CharField(max_length=50, verbose_name = 'Nome')
	descricao = models.TextField(verbose_name = 'Descrição')
	inicio = models.DateTimeField(verbose_name = 'Inicio')
	fim = models.DateTimeField(verbose_name = 'Fim')


class Participe(models.Model):
	idParticipe = models.AutoField(primary_key=True)
	idSelecao = models.IntegerField(verbose_name = 'Id da Seleção')
	idUsuario = models.IntegerField(verbose_name = 'Id do Usuario')

def __str__(self):
	return self.nome