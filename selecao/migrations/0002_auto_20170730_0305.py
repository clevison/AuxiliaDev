# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selecao',
            name='programa',
        ),
        migrations.AddField(
            model_name='selecao',
            name='idPrograma',
            field=models.IntegerField(default=1, verbose_name='Id do programa'),
            preserve_default=False,
        ),
    ]
