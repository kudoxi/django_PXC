# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-17 08:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=64, verbose_name='品牌')),
                ('orderNo', models.CharField(max_length=64, verbose_name='订单号')),
                ('ctitle', models.CharField(max_length=64, verbose_name='车名')),
                ('orderStatus', models.IntegerField(choices=[(0, '未支付'), (1, '已发货'), (2, '已收货')], verbose_name='订单状态')),
                ('isDeleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('register_date', models.DateField(verbose_name='上牌日期')),
                ('engineNo', models.CharField(max_length=64, verbose_name='发动机号')),
                ('mileage', models.IntegerField(verbose_name='公里数')),
                ('maintenance', models.BooleanField(default=False, verbose_name='是否维修')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('extractprice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='成交价格')),
                ('newprice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='新车价格')),
                ('picture', models.ImageField(default='normal.png', upload_to='static/carinfo', verbose_name='图片')),
                ('formalities', models.BooleanField(default=False, verbose_name='是否办好手续')),
                ('debt', models.BooleanField(default=False, verbose_name='是否有债务')),
                ('promise', models.TextField(verbose_name='承诺')),
                ('isPurchase', models.BooleanField(default=False, verbose_name='是否已出售')),
                ('buy_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_user', to=settings.AUTH_USER_MODEL, verbose_name='买家')),
                ('sale_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_user', to=settings.AUTH_USER_MODEL, verbose_name='卖家')),
            ],
            options={
                'verbose_name_plural': '订单',
                'verbose_name': '订单列表',
            },
        ),
    ]