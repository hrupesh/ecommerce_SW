# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_vendor_daily_pl_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_master',
            name='password',
            field=models.CharField(default=2, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor_master',
            name='username',
            field=models.CharField(default=2, max_length=120, unique=True),
            preserve_default=False,
        ),
    ]
