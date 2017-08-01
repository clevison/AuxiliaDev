# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0021_participe_idselecao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participe',
            name='idSelecao',
        ),
    ]
