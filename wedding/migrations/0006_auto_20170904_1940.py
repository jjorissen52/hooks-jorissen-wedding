# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0005_backgroundphoto_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.FileField(blank=True, null=True, upload_to='uploaded_photos')),
                ('description', markupfield.fields.MarkupField(default='No Description Provided', rendered_field=True)),
                ('description_markup_type', models.CharField(blank=True, choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown'), ('restructuredtext', 'Restructured Text')], default=None, max_length=30, null=True)),
                ('page', models.CharField(choices=[('Home', 'Home'), ('Food', 'Food'), ('Contact', 'Contact'), ('Gifts', 'Gifts'), ('Venue', 'Venue'), ('RSVP', 'RSVP')], default='Home', max_length=10)),
                ('_description_rendered', models.TextField(default='No Description Provided', editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='venue',
            name='_description_rendered',
            field=models.TextField(default='No Description Provided', editable=False),
        ),
        migrations.AddField(
            model_name='venue',
            name='description',
            field=markupfield.fields.MarkupField(default='No Description Provided', rendered_field=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='description_markup_type',
            field=models.CharField(blank=True, choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown'), ('restructuredtext', 'Restructured Text')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='backgroundphoto',
            name='page',
            field=models.CharField(choices=[('Home', 'Home'), ('Food', 'Food'), ('Contact', 'Contact'), ('Gifts', 'Gifts'), ('Venue', 'Venue'), ('RSVP', 'RSVP')], default='Home', max_length=10),
        ),
    ]
