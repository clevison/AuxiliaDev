#coding: utf-8
from django.db import models

# Create your models here.
class Programa(models.Model):
	id_programa = models.AutoField(primary_key=True)
	id_criador = models.IntegerField(verbose_name = 'Id do Criador')
	criador = models.CharField(max_length=50, verbose_name = 'Autor')
	titulo = models.CharField(max_length=50, verbose_name = 'Título')
	descricao = models.TextField(verbose_name = 'Descrição')

def __str__(self):
	return self.titulo