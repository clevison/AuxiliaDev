# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0006_selecao_criador'),
    ]

    operations = [
        migrations.AddField(
            model_name='selecao',
            name='participantes',
            field=models.ManyToManyField(to='selecao.Participe'),
        ),
    ]
