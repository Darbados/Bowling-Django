# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-15 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bowling', '0010_frame_total_score_in_frame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='attempt1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='frame',
            name='attempt2',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='frame',
            name='attempt3',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
