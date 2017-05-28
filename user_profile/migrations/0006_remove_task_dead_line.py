# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20170526_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='dead_line',
        ),
    ]
