# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysqlbench', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParraleTestItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workers', models.PositiveIntegerField(default=0, verbose_name='并行度')),
                ('truncations_per_seconde', models.FloatField(default=0, verbose_name='每秒执行完成多少事务')),
                ('duration', models.FloatField(default=0, verbose_name='执行完所有事务所用的总时间')),
            ],
        ),
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=24, verbose_name='测试任务的名称')),
                ('detail', models.CharField(default='', max_length=256, verbose_name='测试任务的详细内容')),
            ],
        ),
        migrations.CreateModel(
            name='TestItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mysql_version', models.CharField(default='', max_length=16, verbose_name='mysql版号')),
                ('variable_name', models.CharField(default='', max_length=24, verbose_name='variable名')),
                ('variable_value', models.CharField(default='', max_length=16, verbose_name='variable值')),
                ('truncations_per_seconde', models.FloatField(default=0, verbose_name='每秒执行完成多少事务')),
                ('duration', models.FloatField(default=0, verbose_name='执行完所有事务所用的总时间')),
                ('host_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysqlbench.HostInfo', verbose_name='主机配置')),
                ('task_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysqlbench.TaskInfo', verbose_name='任务类型')),
            ],
        ),
        migrations.AddField(
            model_name='parraletestitem',
            name='test_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysqlbench.TestItem', verbose_name='测试项'),
        ),
        migrations.AddIndex(
            model_name='testitem',
            index=models.Index(fields=['variable_name', 'variable_value'], name='ix_variable_name_value'),
        ),
        migrations.AlterUniqueTogether(
            name='testitem',
            unique_together=set([('mysql_version', 'variable_name', 'variable_value')]),
        ),
    ]