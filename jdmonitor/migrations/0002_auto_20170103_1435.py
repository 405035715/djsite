# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdmonitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jdmonitor',
            name='hospital_id',
            field=models.IntegerField(verbose_name='医院编码'),
        ),
    ]
