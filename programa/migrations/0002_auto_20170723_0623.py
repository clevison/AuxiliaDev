# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='descricao',
            field=models.TextField(verbose_name='descrição'),
        ),
    ]
