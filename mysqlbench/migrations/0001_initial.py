# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=24, unique=True, verbose_name='主机名(阿里云最小配置)')),
                ('os', models.CharField(default='', max_length=16)),
                ('cores', models.PositiveIntegerField(default=0, verbose_name='cpu 核心数')),
                ('memeroys', models.PositiveIntegerField(default=0, verbose_name='内存大小 MB')),
                ('disks', models.PositiveIntegerField(default=0, verbose_name='数据盘大小 MB')),
                ('is_log_ssd', models.BooleanField(default=False, verbose_name='日志盘是否是ssd')),
                ('is_data_ssd', models.BooleanField(default=False, verbose_name='数据盘是否是ssd')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='hostinfo',
            unique_together=set([('os', 'cores', 'memeroys', 'disks', 'is_log_ssd', 'is_data_ssd')]),
        ),
    ]
