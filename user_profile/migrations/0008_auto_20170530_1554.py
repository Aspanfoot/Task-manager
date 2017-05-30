# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='host',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(related_name='user', default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
