# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0013_auto_20170731_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participe',
            name='idParticipe',
        ),
        migrations.AddField(
            model_name='participe',
            name='id',
            field=models.AutoField(default=1, verbose_name='ID', auto_created=True, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
