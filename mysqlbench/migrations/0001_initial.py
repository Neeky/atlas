# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BenchCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mysql_version', models.CharField(default='', max_length=16, verbose_name='所测试的mysql版号')),
                ('variable_name', models.CharField(default='', max_length=24, verbose_name='测试项具体的variable名称')),
                ('bench_type', models.CharField(default='', max_length=24, verbose_name='测试类型:oltp_insert,oltp_delete ...')),
                ('detail', models.CharField(default='', max_length=256, verbose_name='测试项的详细说明')),
            ],
        ),
        migrations.CreateModel(
            name='BenchCaseInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workers', models.PositiveIntegerField(default=1, verbose_name='并行度')),
                ('variable_value', models.CharField(default='', max_length=16, verbose_name='variable值')),
                ('truncations_per_seconde', models.FloatField(default=0, verbose_name='每秒执行完成多少事务')),
                ('query_per_seconde', models.FloatField(default=0, verbose_name='每秒执行完成多少查询')),
                ('duration', models.FloatField(default=0, verbose_name='执行完所有事务所用的总时间')),
                ('bench_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='mysqlbench.BenchCase', verbose_name='任务类型')),
            ],
        ),
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=24, unique=True, verbose_name='主机名(阿里云最小配置)')),
                ('os', models.CharField(default='', max_length=16)),
                ('cores', models.PositiveIntegerField(default=0, verbose_name='cpu 核心数')),
                ('memorys', models.PositiveIntegerField(default=0, verbose_name='内存大小 MB')),
                ('disks', models.PositiveIntegerField(default=0, verbose_name='数据盘大小 MB')),
                ('is_log_ssd', models.BooleanField(default=False, verbose_name='日志盘是否是ssd')),
                ('is_data_ssd', models.BooleanField(default=False, verbose_name='数据盘是否是ssd')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='hostinfo',
            unique_together=set([('os', 'cores', 'memorys', 'disks', 'is_log_ssd', 'is_data_ssd')]),
        ),
        migrations.AddField(
            model_name='benchcase',
            name='host_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='mysqlbench.HostInfo', verbose_name='主机配置'),
        ),
        migrations.AlterUniqueTogether(
            name='benchcaseinstance',
            unique_together=set([('bench_case', 'variable_value', 'workers')]),
        ),
        migrations.AlterUniqueTogether(
            name='benchcase',
            unique_together=set([('host_info', 'mysql_version', 'variable_name', 'bench_type')]),
        ),
    ]
