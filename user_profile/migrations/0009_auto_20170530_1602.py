# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_auto_20170530_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='host',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
