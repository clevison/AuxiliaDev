# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0011_auto_20170731_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participe',
            name='idParticipe',
        ),
        migrations.RemoveField(
            model_name='participe',
            name='idSelecao',
        ),
        migrations.AddField(
            model_name='participe',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True, default=0),
            preserve_default=False,
        ),
    ]
