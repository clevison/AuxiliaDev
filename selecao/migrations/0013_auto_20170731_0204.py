# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0012_auto_20170731_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participe',
            name='id',
        ),
        migrations.AddField(
            model_name='participe',
            name='idParticipe',
            field=models.AutoField(primary_key=True, default=1, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participe',
            name='nome',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
