# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0004_auto_20170730_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='selecao',
            name='vagas',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
