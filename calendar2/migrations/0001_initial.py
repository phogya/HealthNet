# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('patient', models.CharField(max_length=20, default='default')),
                ('doctor', models.CharField(max_length=20, default='default')),
                ('year', models.CharField(max_length=20, default='default')),
                ('month', models.CharField(max_length=20, default='default')),
                ('day', models.CharField(max_length=20, default='default')),
                ('start_time_hour', models.CharField(max_length=10, default='default')),
                ('start_time_min', models.CharField(max_length=10, default='default')),
                ('start_time_apm', models.CharField(max_length=5, default='default')),
                ('end_time_hour', models.CharField(max_length=10, default='default')),
                ('end_time_min', models.CharField(max_length=10, default='default')),
                ('end_time_apm', models.CharField(max_length=5, default='default')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('hospital', models.CharField(max_length=100, default='default')),
            ],
        ),
    ]
