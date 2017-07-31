# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0008_auto_20170731_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participe',
            name='idParticipe',
        ),
        migrations.AddField(
            model_name='participe',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', default=1, primary_key=True, auto_created=True),
            preserve_default=False,
        ),
    ]
