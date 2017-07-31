# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0003_participe'),
    ]

    operations = [
        migrations.AddField(
            model_name='selecao',
            name='idCriador',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='selecao',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='selecao',
            name='fim',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='selecao',
            name='idPrograma',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='selecao',
            name='inicio',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='selecao',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]
