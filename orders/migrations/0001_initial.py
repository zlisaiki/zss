# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 15:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='订单id')),
                ('keyword', models.CharField(max_length=50, null=True, verbose_name='关键词')),
                ('count', models.IntegerField(default=0, null=True, verbose_name='数量')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18, null=True, verbose_name='金额')),
                ('status', models.IntegerField(null=True, verbose_name='订单状态1.审核2,完成.3,失败,4执行中,5失败,6.审核未通过')),
                ('error_desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('platform', models.CharField(choices=[('taobao', '淘宝'), ('jd', '京东')], max_length=20, null=True, verbose_name='平台')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='最后修改时间')),
                ('remark', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('good', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Good', verbose_name='商品')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Shop', verbose_name='店铺')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'orders',
            },
        ),
    ]
