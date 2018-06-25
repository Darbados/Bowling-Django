from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import uuid
import json
import random
from collections import OrderedDict


class Survey(models.Model):
    SURVEY_STATUS_CREATED = 1
    SURVEY_STATUS_SENT = 2
    SURVEY_STATUS_COMPLETED = 3

    SURVEY_STATUSES = (
        (SURVEY_STATUS_CREATED, 'created'),
        (SURVEY_STATUS_SENT, 'sent'),
        (SURVEY_STATUS_COMPLETED, 'completed'),
    )

    RATING_OPTIONS = list(range(1,6))

    created_at = models.DateTimeField(default=timezone.now)
    unique_value = models.SlugField(max_length=100, default='', blank=True)
    status = models.IntegerField(default=SURVEY_STATUS_CREATED, choices=SURVEY_STATUSES)
    answers = models.TextField(default='')

    def __str__(self):
        return "{0}-{1}".format(self.created_at, self.status)

    @property
    def answers_json(self):
        return json.loads(self.answers)

    def save(self, *args, **kwargs):
        if self.unique_value is '':
            self.unique_value = str(uuid.uuid1())

        self.answers = OrderedDict()

        for x in range(3):
            self.answers["question_{}".format(x+1)] = ["How are you?", random.sample(Survey.RATING_OPTIONS, 1)[0]]
        self.answers = json.dumps(self.answers, ensure_ascii=False)
        super(Survey, self).save(*args, **kwargs)


class RatingQuestion(models.Model):
    RATE_1 = 1
    RATE_2 = 2
    RATE_3 = 3

    RATE_OPTIONS = (
        (RATE_1, '1 star'),
        (RATE_2, '2 stars'),
        (RATE_3, '3 stars'),
    )

    rating = models.CharField(choices=RATE_OPTIONS, max_length=1)
    survey = models.ForeignKey(Survey, related_name='ratings')

    def __str__(self):
        return "Rated as: {}".format(self.rating)