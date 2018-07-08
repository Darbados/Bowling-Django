# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parsers',
            fields=[
                ('id', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('cronjob_id', models.IntegerField(blank=True, null=True)),
                ('sport_id', models.IntegerField(blank=True, null=True)),
                ('source_id', models.IntegerField(blank=True, null=True)),
                ('worker_key', models.CharField(blank=True, default='', help_text='This is a 50 char long unique key which is used for mark who are the records that belongs to its procesing three', max_length=50)),
                ('data_type', models.CharField(choices=[('o', 'odds'), ('re', 'results'), ('ri', 'risks'), ('sch_i', 'scheduled_incidents'), ('i', 'incidents')], default='odds', help_text="enum('odds', 'results' ,'risks') - sets the data type of the parser", max_length=50)),
                ('data_period', models.CharField(blank=True, choices=[('un', 'undefined'), ('ea', 'early'), ('to', 'today'), ('pre', 'prematch'), ('li', 'live')], default='', help_text="sets the data range coverage of the parser - enum('early', 'today', 'prematch', 'live')", max_length=20, null=True)),
                ('eth_binding', models.CharField(blank=True, help_text='used for binding the parser to exact eth0-N  server network interfaces', max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, help_text='specify the date-time when the current parser has been created', null=True)),
                ('last_used_at', models.DateTimeField(blank=True, help_text='specify the date-time when the current parsers has been used for last time', null=True)),
                ('url_template', models.CharField(blank=True, max_length=10000, null=True)),
                ('url_params', models.CharField(blank=True, max_length=10000, null=True)),
                ('has_tubes', models.BooleanField(default=False)),
                ('tubes_time_to_kill', models.IntegerField(blank=True)),
                ('tubes_number', models.IntegerField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('ok', 'ok'), ('error', 'error')], default='ok', max_length=10)),
                ('status_info', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField()),
                ('debug_mode', models.BooleanField()),
                ('debug_level', models.BooleanField()),
                ('loop_current', models.IntegerField(blank=True)),
                ('loop_maximum', models.IntegerField(blank=True)),
                ('loop_started_at', models.DateTimeField(blank=True, null=True)),
                ('loop_fnished_at', models.DateTimeField(blank=True, null=True)),
                ('data_count', models.IntegerField(blank=True)),
                ('has_login', models.BooleanField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'parsers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('port', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('country_id', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'db_table': 'proxies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Source_Proxies',
            fields=[
                ('id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('source_id', models.IntegerField(blank=True, null=True)),
                ('proxy_id', models.IntegerField(blank=True, null=True)),
                ('used', models.IntegerField(blank=True, null=True)),
                ('used_limit', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField()),
                ('used_at', models.DateTimeField(blank=True, null=True)),
                ('uncalled', models.IntegerField(blank=True, null=True)),
                ('reset_at', models.DateTimeField(blank=True, null=True)),
                ('empty_api_responses_num', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'source_proxies',
                'managed': False,
            },
        ),
    ]
