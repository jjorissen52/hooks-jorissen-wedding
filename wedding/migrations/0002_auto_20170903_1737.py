# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 22:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='event',
            name='start',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='venue',
            name='alcohol_situation',
            field=models.CharField(choices=[('0', 'Alcohol provider of choice'), ('1', 'Alcohol provided by venue'), ('2', 'No Alcohol')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='venue',
            name='food_situation',
            field=models.CharField(choices=[('0', 'Must use provided catering'), ('1', 'Must choose from approved caterers'), ('2', 'Any caterer is fine')], default=1, max_length=1),
        ),
    ]