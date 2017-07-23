#coding: utf-8
from django.db import models

# Create your models here.
class Programa(models.Model):
    criador = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(verbose_name = 'descrição')

def __str__(self):
	return self.titulo