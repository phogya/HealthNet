# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admission_Discharge', '0003_remove_admission_discharge_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission_discharge',
            name='hospital',
        ),
        migrations.AddField(
            model_name='admission_discharge',
            name='patient_id',
            field=models.CharField(default='default', max_length=200),
        ),
        migrations.AddField(
            model_name='admission_discharge',
            name='status',
            field=models.CharField(default='default', max_length=200),
        ),
        migrations.AlterField(
            model_name='admission_discharge',
            name='date_admitted',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='admission_discharge',
            name='date_discharged',
            field=models.CharField(max_length=100),
        ),
    ]
