# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-01 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=16)),
                ('nick_name', models.CharField(default='', max_length=16)),
                ('id_card_number', models.CharField(default='', max_length=18)),
                ('email_addr', models.EmailField(max_length=254)),
                ('mobile_phone', models.CharField(max_length=11)),
                ('wechat', models.CharField(default='', max_length=24)),
                ('qq', models.BigIntegerField(default=0)),
                ('last_login_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_ip', models.GenericIPAddressField(default='0.0.0.0')),
                ('password', models.CharField(default='', max_length=24)),
                ('actived', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AlterIndexTogether(
            name='user',
            index_together=set([('email_addr', 'password')]),
        ),
    ]
