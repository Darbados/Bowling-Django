# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Here will be the source_proxies table represented as a django model, which will be not managed from django


class Source_Proxies(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    source_id = models.IntegerField(null=True, blank=True)
    proxy_id = models.IntegerField(null=True, blank=True)
    used = models.IntegerField(null=True, blank=True)
    used_limit = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(blank=True)
    used_at = models.DateTimeField(null=True, blank=True)
    uncalled = models.IntegerField(null=True, blank=True)
    reset_at = models.DateTimeField(null=True, blank=True)
    empty_api_responses_num = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'proxies_service'
        managed = False
        db_table = 'source_proxies'

class Proxy(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    address = models.CharField(null=True, max_length=50, blank=True)
    port = models.CharField(null=True, max_length=10, blank=True)
    type = models.CharField(null=True, max_length=10, blank=True)
    country_id = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(blank=True)

    class Meta:
        app_label = "proxies_service"
        managed = False
        db_table = 'proxies'

class Parsers(models.Model):

    DATA_TYPE = (
        ('o','odds'),
        ('re','results'),
        ('ri','risks'),
        ('sch_i','scheduled_incidents'),
        ('i','incidents')
    )
    DATA_PERIOD = (
        ('un','undefined'),
        ('ea','early'),
        ('to','today'),
        ('pre','prematch'),
        ('li','live')
    )

    statuses = (
        ('ok','ok'),
        ('error','error')
    )

    id = models.AutoField(primary_key=True, max_length=5)
    cronjob_id = models.IntegerField(null=True, blank=True)
    sport_id = models.IntegerField(null=True, blank=True)
    source_id = models.IntegerField(null=True, blank=True)
    worker_key = models.CharField(max_length=50, blank=True, default='',help_text="This is a 50 char long unique key which is used for mark who are the records that belongs to its procesing three")
    data_type = models.CharField(choices=DATA_TYPE,max_length=50,default='odds',help_text="enum('odds', 'results' ,'risks') - sets the data type of the parser")
    data_period = models.CharField(choices=DATA_PERIOD, null=True, blank=True,default='', max_length=20, help_text="sets the data range coverage of the parser - enum('early', 'today', 'prematch', 'live')")
    eth_binding = models.CharField(null=True,blank=True,max_length=255,help_text="used for binding the parser to exact eth0-N  server network interfaces")
    created_at = models.DateTimeField(null=True, blank=True, help_text="specify the date-time when the current parser has been created")
    last_used_at = models.DateTimeField(null=True, blank=True, help_text="specify the date-time when the current parsers has been used for last time")
    url_template = models.CharField(max_length=10000, null=True, blank=True)
    url_params = models.CharField(max_length=10000, null=True, blank=True)
    has_tubes = models.BooleanField(default=False, blank=True)
    tubes_time_to_kill = models.IntegerField(blank=True)
    tubes_number = models.IntegerField(blank=True)
    status = models.CharField(choices=statuses, default='ok', blank=True, max_length=10)
    status_info = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(blank=True)
    debug_mode = models.BooleanField(blank=True)
    debug_level = models.BooleanField(blank=True)
    loop_current = models.IntegerField(blank=True)
    loop_maximum = models.IntegerField(blank=True)
    loop_started_at = models.DateTimeField(null=True, blank=True)
    loop_fnished_at = models.DateTimeField(null=True, blank=True)
    data_count = models.IntegerField( blank=True)
    has_login = models.BooleanField(blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        app_label = "proxies_service"
        managed = False
        db_table = "parsers"