# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0002_auto_20170723_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programa',
            name='id',
        ),
        migrations.AddField(
            model_name='programa',
            name='id_prog',
            field=models.AutoField(primary_key=True, default=1, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='programa',
            name='criador',
            field=models.CharField(max_length=50, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='Título'),
        ),
    ]
