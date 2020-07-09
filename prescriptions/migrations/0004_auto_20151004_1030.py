# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0003_auto_20151004_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='date_issued',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='pat_dob',
        ),
        migrations.AddField(
            model_name='prescription',
            name='dose',
            field=models.CharField(max_length=200, default='200 mg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='refill',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 10, 4, 14, 30, 14, 901618, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
