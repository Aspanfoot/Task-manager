# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20170526_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(default=b'NORMAL', max_length=9, choices=[(b'LOW', b'Low'), (b'NORMAL', b'Normal'), (b'HIGH', b'High')]),
        ),
    ]
