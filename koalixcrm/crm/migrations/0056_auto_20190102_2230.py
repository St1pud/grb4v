# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-02 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0055_auto_20181022_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.ProductType', verbose_name='Product'),
        ),
    ]