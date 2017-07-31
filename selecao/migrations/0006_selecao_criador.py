# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0005_selecao_vagas'),
    ]

    operations = [
        migrations.AddField(
            model_name='selecao',
            name='criador',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
