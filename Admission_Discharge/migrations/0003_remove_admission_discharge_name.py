# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admission_Discharge', '0002_admission_discharge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission_discharge',
            name='name',
        ),
    ]
