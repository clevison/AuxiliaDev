# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0019_auto_20170731_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participe',
            name='idUsuario',
            field=models.IntegerField(),
        ),
    ]
