# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0004_auto_20170904_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundphoto',
            name='page',
            field=models.CharField(default='Home', max_length=10),
        ),
    ]