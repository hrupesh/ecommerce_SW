# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0019_remove_approved_pl_by_loma_list_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approved_pl_by_loma',
            old_name='offer_price',
            new_name='cal_offer_price',
        ),
    ]