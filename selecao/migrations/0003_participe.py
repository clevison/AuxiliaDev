# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0002_auto_20170730_0305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participe',
            fields=[
                ('idParticipe', models.AutoField(primary_key=True, serialize=False)),
                ('idSelecao', models.IntegerField(verbose_name='Id da Seleção')),
                ('idUsuario', models.IntegerField(verbose_name='Id do Usuario')),
            ],
        ),
    ]
