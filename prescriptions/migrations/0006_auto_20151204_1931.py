# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0005_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='patient_name',
        ),
        migrations.AddField(
            model_name='prescription',
            name='patient_id',
            field=models.CharField(default='default', max_length=200),
        ),
    ]
