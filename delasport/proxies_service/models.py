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