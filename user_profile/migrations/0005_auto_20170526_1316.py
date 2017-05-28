# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_task_dead_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dead_line',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
