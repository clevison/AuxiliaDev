# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0015_auto_20170731_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participe',
            name='idParticipe',
        ),
        migrations.AddField(
            model_name='participe',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
