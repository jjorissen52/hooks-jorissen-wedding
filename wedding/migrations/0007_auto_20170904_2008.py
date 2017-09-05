# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0006_auto_20170904_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='description_markup_type',
            field=models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown'), ('restructuredtext', 'Restructured Text')], default='markdown', max_length=30),
        ),
        migrations.AlterField(
            model_name='venue',
            name='description_markup_type',
            field=models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown'), ('restructuredtext', 'Restructured Text')], default='markdown', max_length=30),
        ),
    ]