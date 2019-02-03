# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-19 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colorex', '0003_auto_20180512_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level_10_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level_1_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level_1_unlock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level_2_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level_3_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level_4_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level_5_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level_6_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level_7_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level_8_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level_9_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='total_time',
            field=models.CharField(blank=True, default='0', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, default='Anonymous', max_length=500, null=True),
        ),
    ]
