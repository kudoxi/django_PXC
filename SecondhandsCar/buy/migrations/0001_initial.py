# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-17 08:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=64, verbose_name='品牌')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('mileage', models.IntegerField(verbose_name='公里数')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.CarInfo', verbose_name='汽车')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '购买意愿列表',
                'verbose_name_plural': '购买意愿',
            },
        ),
    ]
