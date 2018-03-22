from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Game(models.Model):
    total_score = models.IntegerField(default=0)
    player = models.CharField(max_length=50, default="")
    start_date = models.DateTimeField("date started", default=timezone.now)
    end_date = models.DateTimeField("date ended", default=timezone.now)

    def __str__(self):
        return self.player

class Frame(models.Model):
    game = models.ForeignKey(Game, related_name="frames" ,on_delete=models.CASCADE)
    attempt1 = models.IntegerField(default=0)
    attempt2 = models.IntegerField(default=0, blank=True)
    attempt3 = models.IntegerField(default=0, blank=True)
    total_score_in_frame = models.IntegerField(default=0)
