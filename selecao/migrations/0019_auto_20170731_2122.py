# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0018_auto_20170731_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participe',
            name='idUsuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
