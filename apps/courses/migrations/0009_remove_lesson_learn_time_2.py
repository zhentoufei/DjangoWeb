# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-24 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_lesson_learn_time_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='learn_time_2',
        ),
    ]
