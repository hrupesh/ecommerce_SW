# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-05 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0026_auto_20190204_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daily_price_list',
            old_name='vendor_daily_id',
            new_name='vendor_id',
        ),
    ]
