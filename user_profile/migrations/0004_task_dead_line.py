# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dead_line',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
