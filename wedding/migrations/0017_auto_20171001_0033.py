# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 05:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0016_auto_20170930_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='alcohol_pricing',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='alcohol_situation',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='allotted_hours',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='base_price',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='food_situation',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='logistics_comments',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='price_per_hour',
        ),
    ]
