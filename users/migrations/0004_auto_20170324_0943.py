# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_authuser_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=18, null=True, verbose_name='账户余额'),
        ),
    ]
