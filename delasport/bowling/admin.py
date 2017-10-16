from django.contrib import admin
from .models import Game, Frame
# Register your models here.

class FrameInline(admin.TabularInline):
    model = Frame

class GameAdmin(admin.ModelAdmin):
    list_display = ('id','total_score','player')
    inlines = [FrameInline]

admin.site.register(Game, GameAdmin)
