# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0005_auto_20170724_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selecao',
            fields=[
                ('idSelecao', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('inicio', models.DateTimeField(verbose_name='Inicio')),
                ('fim', models.DateTimeField(verbose_name='Fim')),
                ('programa', models.ForeignKey(to='programa.Programa')),
            ],
        ),
    ]
