from programa.models import Programa

from django.db import models


# Create your models here.
class Participe(models.Model):
	# idParticipe = models.AutoField(primary_key=True)
	# idSelecao = models.IntegerField(verbose_name = 'Id da Seleção')
	# idSelecao = models.ForeignKey('Selecao', on_delete=models.CASCADE)
	idUsuario = models.IntegerField()
	nome = models.CharField(max_length=50)

def __str__(self):
	return self.nome


class Selecao(models.Model):
	idSelecao = models.AutoField(primary_key=True)
	idCriador = models.IntegerField()
	criador = models.CharField(max_length=50)
	idPrograma = models.IntegerField()
	# idPrograma = models.ForeignKey('programa.Programa', on_delete=models.CASCADE)
	nome = models.CharField(max_length=50)
	descricao = models.TextField()
	inicio = models.DateTimeField()
	fim = models.DateTimeField()
	vagas = models.IntegerField()
	participantes = models.ManyToManyField(Participe)

def __str__(self):
	return self.nome
