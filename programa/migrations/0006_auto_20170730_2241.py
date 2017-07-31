# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0005_auto_20170724_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programa',
            old_name='id_criador',
            new_name='idCriador',
        ),
        migrations.RenameField(
            model_name='programa',
            old_name='id_programa',
            new_name='idPrograma',
        ),
    ]
