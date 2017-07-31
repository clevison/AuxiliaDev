#coding: utf-8
from django.db import models

# Create your models here.
class Programa(models.Model):
	idPrograma = models.AutoField(primary_key=True)
	idCriador = models.IntegerField()
	criador = models.CharField(max_length=50)
	titulo = models.CharField(max_length=50)
	descricao = models.TextField()

def __str__(self):
	return self.titulo