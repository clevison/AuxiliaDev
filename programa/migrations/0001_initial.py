# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('criador', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
