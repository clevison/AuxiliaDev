# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0004_programa_id_cria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programa',
            old_name='id_cria',
            new_name='id_criador',
        ),
        migrations.RenameField(
            model_name='programa',
            old_name='id_prog',
            new_name='id_programa',
        ),
    ]
