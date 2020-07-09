# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date_issued', models.DateField(auto_created=True, verbose_name='Date issued')),
                ('patient_name', models.CharField(max_length=200)),
                ('medication', models.CharField(max_length=200)),
                ('pat_DOB', models.DateField(verbose_name='Patient Date of Birth')),
            ],
        ),
    ]
