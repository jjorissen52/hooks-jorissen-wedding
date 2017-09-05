# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0007_auto_20170904_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='content',
            name='rank',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='display_description',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='rank',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
