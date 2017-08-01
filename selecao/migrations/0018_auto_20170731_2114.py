# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0017_remove_participe_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selecao',
            name='participantes',
            field=models.ManyToManyField(blank=True, null=True, to='selecao.Participe'),
        ),
    ]
