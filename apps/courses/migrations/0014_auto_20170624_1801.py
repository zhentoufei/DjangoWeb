# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-24 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20170624_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='\u8001\u5e08\u544a\u8bc9\u4f60', max_length=30, verbose_name='\u8001\u5e08\u544a\u8bc9\u4f60'),
        ),
        migrations.AlterField(
            model_name='course',
            name='you_need_know',
            field=models.CharField(default='\u8bfe\u7a0b\u987b\u77e5', max_length=30, verbose_name='\u8bfe\u7a0b\u987b\u77e5'),
        ),
    ]
