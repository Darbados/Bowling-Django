# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-19 18:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bowlingREST', '0004_auto_20171019_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='counterFrames',
        ),
    ]
