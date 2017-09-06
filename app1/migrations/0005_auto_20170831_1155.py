# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-31 11:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20170831_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airmach',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='autoswitch',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='boiler',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='configsun',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='设置时间'),
        ),
        migrations.AlterField(
            model_name='configtemp',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='设置时间'),
        ),
        migrations.AlterField(
            model_name='configwater',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='设置时间'),
        ),
        migrations.AlterField(
            model_name='eleccolorcount',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='electimecount',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='factorydata',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='fireprosys',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='pipe',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='rotorcolorcount',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='rotortimecount',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='sendtomqtt',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='switchcontrol1',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='switchcontrol2',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='switchcontrol3',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='switchcontrol4',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='watertower',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]