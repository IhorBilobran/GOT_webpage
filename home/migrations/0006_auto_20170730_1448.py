# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_person_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='img',
            field=models.ImageField(blank=True, upload_to='persons_image/', verbose_name='emblem'),
        ),
    ]
