# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20170323_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faccounttransfer',
            options={'verbose_name': '充值&提现', 'verbose_name_plural': '充值&提现列表'},
        ),
        migrations.AlterField(
            model_name='faccounttransfer',
            name='status',
            field=models.IntegerField(choices=[(0, '审核不通过'), (1, '审核通过'), (2, '待审核')], null=True, verbose_name='审核状态'),
        ),
        migrations.AlterField(
            model_name='faccounttransfer',
            name='transfertype',
            field=models.CharField(choices=[('inpour', '充值'), ('withdraw', '提现')], max_length=20, null=True, verbose_name='交易类型'),
        ),
    ]