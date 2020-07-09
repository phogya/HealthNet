# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0002_auto_20151004_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='dose',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='refill',
        ),
        migrations.AddField(
            model_name='prescription',
            name='date_issued',
            field=models.DateField(verbose_name='Date issued', default=datetime.datetime(2015, 10, 4, 14, 23, 59, 209130, tzinfo=utc), auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='pat_dob',
            field=models.DateField(verbose_name='Patient Date of Birth', default=datetime.datetime(2015, 10, 4, 14, 24, 4, 829451, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
