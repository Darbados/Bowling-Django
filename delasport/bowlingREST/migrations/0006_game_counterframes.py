# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-19 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bowlingREST', '0005_remove_game_counterframes'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='counterFrames',
            field=models.IntegerField(default=1),
        ),
    ]
