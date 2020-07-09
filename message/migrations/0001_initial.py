# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=30)),
                ('receiver', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=2000)),
                ('time', models.DateTimeField()),
                ('read', models.BooleanField()),
            ],
        ),
    ]
