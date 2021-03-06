# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 20:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0008_auto_20170731_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='goods/%Y/%m/%d')),
                ('avaliable', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('reference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.House')),
            ],
        ),
    ]
