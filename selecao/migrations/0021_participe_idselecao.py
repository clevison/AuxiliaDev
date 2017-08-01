# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0020_auto_20170731_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='participe',
            name='idSelecao',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
