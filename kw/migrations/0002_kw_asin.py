# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-26 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kw',
            name='asin',
            field=models.CharField(max_length=250, null=True, verbose_name='Asin'),
        ),
    ]