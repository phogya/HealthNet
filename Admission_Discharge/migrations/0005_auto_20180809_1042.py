# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admission_Discharge', '0004_auto_20151205_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission_discharge',
            name='date_admitted',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='admission_discharge',
            name='date_discharged',
            field=models.DateTimeField(null=True),
        ),
    ]
