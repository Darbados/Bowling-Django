from __future__ import unicode_literals

from django.db import models

class Game(models.Model):
    total_score = models.IntegerField(default=0)
    player = models.CharField(max_length=50, default="")
    roll1 = models.IntegerField(default=0)
    roll2 = models.IntegerField(default=0)
    roll3 = models.IntegerField(default=0)
    roll4 = models.IntegerField(default=0)
    roll5 = models.IntegerField(default=0)
    roll6 = models.IntegerField(default=0)
    roll7 = models.IntegerField(default=0)
    roll8 = models.IntegerField(default=0)
    roll9 = models.IntegerField(default=0)
    roll10 = models.IntegerField(default=0)
    roll11 = models.IntegerField(default=0)
    roll12 = models.IntegerField(default=0)
    roll13 = models.IntegerField(default=0)
    roll14 = models.IntegerField(default=0)
    roll15 = models.IntegerField(default=0)
    roll16 = models.IntegerField(default=0)
    roll17 = models.IntegerField(default=0)
    roll18 = models.IntegerField(default=0)
    roll19 = models.IntegerField(default=0)
    roll20 = models.IntegerField(default=0)
    roll21 = models.IntegerField(default=0)
    counterFrames = models.IntegerField(default=1)

    def __str__(self):
        return self.player
