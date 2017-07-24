# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0003_auto_20170724_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='programa',
            name='id_cria',
            field=models.IntegerField(default=1, verbose_name='Id do Criador'),
            preserve_default=False,
        ),
    ]
