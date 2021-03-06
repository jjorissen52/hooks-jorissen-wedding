# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0010_remove_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='rank',
            field=models.PositiveSmallIntegerField(help_text='Lower is better.'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='rank',
            field=models.PositiveSmallIntegerField(help_text='Lower is better.'),
        ),
    ]
