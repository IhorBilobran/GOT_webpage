# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20170803_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='default_pic'),
        ),
    ]
