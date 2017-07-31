# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0009_auto_20170731_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participe',
            name='id',
        ),
        migrations.AddField(
            model_name='participe',
            name='idParticipe',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
