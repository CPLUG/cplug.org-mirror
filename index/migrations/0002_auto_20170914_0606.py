# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='14-250', max_length=50, verbose_name='Location'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='officer',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
    ]
