# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Admission_Discharge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_Discharge',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('hospital', models.CharField(max_length=200)),
                ('date_admitted', models.DateTimeField(default=datetime.datetime.now, blank=True, max_length=200)),
                ('date_discharged', models.CharField(default=datetime.datetime.now, blank=True, max_length=200)),
                ('reason', models.CharField(max_length=200)),
            ],
        ),
    ]
