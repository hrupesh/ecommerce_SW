# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-04 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20190203_1839'),
        ('Loma', '0023_remove_daily_price_list_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loma_operation_model',
            old_name='Loma_master',
            new_name='Zone',
        ),
        migrations.AddField(
            model_name='daily_price_list',
            name='product',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
    ]