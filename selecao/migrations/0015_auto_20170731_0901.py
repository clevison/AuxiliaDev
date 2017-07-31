# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0014_auto_20170731_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participe',
            name='id',
        ),
        migrations.AddField(
            model_name='participe',
            name='idParticipe',
            field=models.AutoField(serialize=False, primary_key=True, default=1),
            preserve_default=False,
        ),
    ]
