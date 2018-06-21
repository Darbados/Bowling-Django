from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import uuid


class Survey(models.Model):
    SURVEY_STATUS_CREATED = 1
    SURVEY_STATUS_SENT = 2
    SURVEY_STATUS_COMPLETED = 3

    SURVEY_STATUSES = (
        (SURVEY_STATUS_CREATED, 'created'),
        (SURVEY_STATUS_SENT, 'sent'),
        (SURVEY_STATUS_COMPLETED, 'completed'),
    )

    created_at = models.DateTimeField(default=timezone.now)
    unique_value = models.SlugField(max_length=100, default='', blank=True)
    status = models.IntegerField(default=SURVEY_STATUS_CREATED, choices=SURVEY_STATUSES)

    def __str__(self):
        return "{0}-{1}".format(self.created_at, self.status)

    def save(self, *args, **kwargs):
        if self.unique_value is '':
            self.unique_value = str(uuid.uuid1())
        super(Survey, self).save(*args, **kwargs)