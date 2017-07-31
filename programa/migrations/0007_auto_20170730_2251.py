# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0006_auto_20170730_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='criador',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='programa',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='programa',
            name='idCriador',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='programa',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
