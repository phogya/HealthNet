# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('trigger', models.CharField(max_length=10000)),
                ('user', models.CharField(max_length=10000)),
                ('action', models.CharField(max_length=10000)),
                ('info', models.CharField(max_length=10000)),
                ('patient', models.CharField(max_length=10000)),
                ('comment', models.CharField(max_length=10000)),
            ],
        ),
    ]
