# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0010_auto_20170731_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participe',
            name='idSelecao',
            field=models.IntegerField(verbose_name='Id da Seleção'),
        ),
    ]
