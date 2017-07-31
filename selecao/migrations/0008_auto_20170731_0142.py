# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0007_selecao_participantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participe',
            name='idSelecao',
            field=models.ForeignKey(to='selecao.Selecao'),
        ),
        migrations.AlterField(
            model_name='participe',
            name='idUsuario',
            field=models.IntegerField(),
        ),
    ]
