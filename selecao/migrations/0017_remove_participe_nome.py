# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0016_auto_20170731_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participe',
            name='nome',
        ),
    ]
