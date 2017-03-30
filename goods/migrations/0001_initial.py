# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 15:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pgood_id', models.CharField(max_length=50, null=True, verbose_name='平台商品id')),
                ('sendaddress', models.CharField(max_length=50, null=True, verbose_name='发货地')),
                ('image1', models.ImageField(default='image/default.png', null=True, upload_to='image/tbgoods/%Y/%m')),
                ('image2', models.ImageField(default='image/default.png', null=True, upload_to='image/tbgoods/%Y/%m')),
                ('image3', models.ImageField(default='image/default.png', null=True, upload_to='image/tbgoods/%Y/%m')),
                ('keyword1', models.CharField(max_length=50, null=True, verbose_name='1关键词')),
                ('price1', models.FloatField(max_length=50, null=True, verbose_name='1价格')),
                ('remark1', models.CharField(max_length=50, null=True, verbose_name='1备注')),
                ('keyword2', models.CharField(max_length=50, null=True, verbose_name='1关键词')),
                ('price2', models.FloatField(max_length=50, null=True, verbose_name='2价格')),
                ('remark2', models.CharField(max_length=50, null=True, verbose_name='2备注')),
                ('keyword3', models.CharField(max_length=50, null=True, verbose_name='3关键词')),
                ('price3', models.FloatField(max_length=50, null=True, verbose_name='3价格')),
                ('remark3', models.CharField(max_length=50, null=True, verbose_name='3备注')),
                ('keyword4', models.CharField(max_length=50, null=True, verbose_name='4关键词')),
                ('price4', models.FloatField(max_length=50, null=True, verbose_name='4价格')),
                ('remark4', models.CharField(max_length=50, null=True, verbose_name='4备注')),
                ('keywor5', models.CharField(max_length=50, null=True, verbose_name='5关键词')),
                ('price5', models.FloatField(max_length=50, null=True, verbose_name='5价格')),
                ('remark5', models.CharField(max_length=50, null=True, verbose_name='5备注')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=50, null=True, verbose_name='店铺名称')),
                ('sellername', models.CharField(max_length=50, null=True, verbose_name='掌柜名称')),
                ('platform', models.CharField(choices=[('taobao', '淘宝'), ('jd', '京东')], max_length=20, null=True, verbose_name='店铺平台')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '店铺名',
                'verbose_name_plural': '店铺名',
                'db_table': 'shops',
            },
        ),
    ]
