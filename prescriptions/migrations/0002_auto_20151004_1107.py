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
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 10, 4, 15, 7, 13, 357796, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='refill',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 10, 4, 15, 7, 23, 524728, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
