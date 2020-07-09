# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='date_issued',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='pat_DOB',
        ),
        migrations.AddField(
            model_name='prescription',
            name='dose',
            field=models.CharField(default=datetime.datetime(2015, 10, 4, 14, 18, 45, 876208, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='refill',
            field=models.CharField(default=datetime.datetime(2015, 10, 4, 14, 19, 3, 356208, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
