# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-31 03:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20170831_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightstatus',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
