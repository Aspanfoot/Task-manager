# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='header',
            new_name='name',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'NOT_STARTED', max_length=12, choices=[(b'COMPLETE', b'Complete'), (b'NOT_STARTED', b'Not Started'), (b'IN_PROGRES', b'In Progres')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
