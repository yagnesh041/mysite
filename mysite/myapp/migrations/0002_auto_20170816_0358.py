# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-15 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='city',
        ),
        migrations.RemoveField(
            model_name='student',
            name='province',
        ),
    ]
