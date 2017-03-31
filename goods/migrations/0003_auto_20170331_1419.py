# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 14:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20170320_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image1',
            field=models.ImageField(blank=True, default='image/default.png', null=True, upload_to='image/tbgoods/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='good',
            name='image2',
            field=models.ImageField(blank=True, default='image/default.png', null=True, upload_to='image/tbgoods/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='good',
            name='image3',
            field=models.ImageField(blank=True, default='image/default.png', null=True, upload_to='image/tbgoods/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='good',
            name='keywor5',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='5关键词'),
        ),
        migrations.AlterField(
            model_name='good',
            name='keyword1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='1关键词'),
        ),
        migrations.AlterField(
            model_name='good',
            name='keyword2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='1关键词'),
        ),
        migrations.AlterField(
            model_name='good',
            name='keyword3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='3关键词'),
        ),
        migrations.AlterField(
            model_name='good',
            name='keyword4',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='4关键词'),
        ),
        migrations.AlterField(
            model_name='good',
            name='pgood_id',
            field=models.CharField(max_length=50, verbose_name='平台商品id'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price1',
            field=models.FloatField(blank=True, default=None, max_length=50, null=True, verbose_name='1价格'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price2',
            field=models.FloatField(blank=True, default=None, max_length=50, null=True, verbose_name='2价格'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price3',
            field=models.FloatField(blank=True, default=None, max_length=50, null=True, verbose_name='3价格'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price4',
            field=models.FloatField(blank=True, max_length=50, null=True, verbose_name='4价格'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price5',
            field=models.FloatField(blank=True, default=None, max_length=50, null=True, verbose_name='5价格'),
        ),
        migrations.AlterField(
            model_name='good',
            name='remark1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='1备注'),
        ),
        migrations.AlterField(
            model_name='good',
            name='remark2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='2备注'),
        ),
        migrations.AlterField(
            model_name='good',
            name='remark3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='3备注'),
        ),
        migrations.AlterField(
            model_name='good',
            name='remark4',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='4备注'),
        ),
        migrations.AlterField(
            model_name='good',
            name='remark5',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='5备注'),
        ),
        migrations.AlterField(
            model_name='good',
            name='sendaddress',
            field=models.CharField(max_length=50, verbose_name='发货地'),
        ),
        migrations.AlterField(
            model_name='good',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Shop', verbose_name='所属店铺'),
        ),
        migrations.AlterField(
            model_name='good',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='platform',
            field=models.CharField(choices=[('taobao', '淘宝'), ('jd', '京东')], max_length=20, verbose_name='店铺平台'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='sellername',
            field=models.CharField(max_length=50, verbose_name='掌柜名称'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shopname',
            field=models.CharField(max_length=50, verbose_name='店铺名称'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
