from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('id','total_score','player','roll1','roll2','roll3','roll4','roll5','roll6','roll7','roll8','roll9','roll10','roll11','roll2','roll13','roll14','roll15','roll16','roll17','roll18','roll19','roll20','roll21')

admin.site.register(Game, GameAdmin)
