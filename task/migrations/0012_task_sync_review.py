# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-17 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_task_log_tid'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='sync_review',
            field=models.IntegerField(default=0),
        ),
    ]