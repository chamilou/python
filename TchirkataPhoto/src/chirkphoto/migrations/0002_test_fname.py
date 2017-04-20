# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chirkphoto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='fname',
            field=models.CharField(max_length=50, default=datetime.date(2015, 3, 25)),
            preserve_default=False,
        ),
    ]
