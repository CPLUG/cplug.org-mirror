# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-19 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20170914_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='first',
            field=models.CharField(blank=True, max_length=50, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='officer',
            name='picture',
            field=models.ImageField(blank=True, upload_to='/events', verbose_name='Picture'),
        ),
    ]
