from __future__ import unicode_literals

import hashlib

from django.db import models
from django.utils import timezone
import uuid
import json
import random
from collections import OrderedDict


class Survey(models.Model):
    SURVEY_STATUS_CREATED = 1
    SURVEY_STATUS_SENT = 2
    SURVEY_STATUS_ANSWERED = 3

    SURVEY_STATUSES = (
        (SURVEY_STATUS_CREATED, 'created'),
        (SURVEY_STATUS_SENT, 'send'),
        (SURVEY_STATUS_ANSWERED, 'answered'),
    )

    survey_unique_value = models.SlugField(
        max_length=100,
        default='',
    )
    status = models.IntegerField(
        default=SURVEY_STATUS_CREATED,
        choices=SURVEY_STATUSES,
    )
    user_comment = models.TextField(
        default='',
    )
    internal_comment = models.TextField(
        default='',
    )

    created_at = models.DateTimeField(
        default=timezone.now,
    )

    updated_at = models.DateTimeField(
        default=timezone.now,
    )

    def __str__(self):
        return 'Survey {0}, {1}'.format(self.id, self.created_at)

    @classmethod
    def get_random_string(cls):
        return str(uuid.uuid1())


class Question(models.Model):
    QUESTION_SINGLE_SELECT = 2
    QUESTION_MULTIPLE_SELECT = 3
    QUESTION_RATTING = 4

    QUESTION_OPEN_END_COMMENT = 'What you would like to be changed?'

    QUESTION_SINGLE_SELECT_ANSWER_YES = 'Yes'
    QUESTION_SINGLE_SELECT_ANSWER_NO = 'No'

    QUESTION_RATTING_OPTIONS = 5

    QUESTION_STATUS_ACTIVE = 1
    QUESTION_STATUS_INACTIVE = 0

    QUESTION_TYPES = (
        (QUESTION_SINGLE_SELECT, 'Yes / No'),
        (QUESTION_RATTING, 'rating'),
    )

    QUESTION_STATUSES = (
        (QUESTION_STATUS_ACTIVE, 'active'),
        (QUESTION_STATUS_INACTIVE, 'inactive'),
    )

    question_text = models.TextField()
    question_type = models.IntegerField(
        default=QUESTION_RATTING,
        choices=QUESTION_TYPES,
    )
    status = models.IntegerField(
        default=QUESTION_STATUS_ACTIVE,
        choices=QUESTION_STATUSES,
    )
    number = models.IntegerField(default=0)

    def __unicode__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        super(Question, self).save(*args, **kwargs)

        if self.question_type == Question.QUESTION_SINGLE_SELECT_ANSWER_NO:
            Responses.objects.create(
                question=self,
                response_text=Question.QUESTION_SINGLE_SELECT_ANSWER_YES,
            )
            Responses.objects.create(
                question=self,
                response_text=Question.QUESTION_SINGLE_SELECT_ANSWER_NO,
            )
        elif self.question_type == Question.QUESTION_RATTING:
            responses = Question.QUESTION_RATTING_OPTIONS
            question = Question.objects.get(id=self.id)
            while responses > 0:
                resp = Responses.objects.create(
                    question=question,
                    response_text=str(responses),
                )
                resp.save()
                responses -= 1


class Responses(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='responses',
        on_delete=models.CASCADE,
    )
    response_text = models.CharField(
        default='',
        max_length=255,
    )

    def __unicode__(self):
        return '{0} response {1}'.format(self.question, self.response_text)


class Answers(models.Model):
    answer = models.IntegerField()
    survey = models.ForeignKey(
        Survey,
        related_name='answers',
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return 'Survey {0}, Question {1}, Answers: {2}'.format(
            self.survey.id,
            self.question.number,
            self.answer,
        )