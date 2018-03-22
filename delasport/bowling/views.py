from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from models import Frame, Game
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from serializers import GameSerializer
from forms import NameForm, FrameForm
from methods import *
from collections import OrderedDict
from django.utils import timezone
from datetime import datetime

class NameView(View):
    def get(self, request):
        form = NameForm()
        template = 'bowling/index.html'
        return render(request, template, {'form': form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            game = Game.objects.create(player=name, start_date=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
        return HttpResponseRedirect(reverse('bowling:add_roll', args=(game.id,)))

class Add_Roll(View):
    def get(self, request, game_id):
        form = FrameForm()
        game = Game.objects.get(id=game_id)
        recordedFrames = game.frames.all()
        rolls_live = [[x.attempt1, x.attempt2, x.attempt3] for x in recordedFrames]
        results = [x.total_score_in_frame for x in recordedFrames]
        try:
            results[0]
            results = re_calculate(rolls_live, results, results[0])
        except IndexError:
            results = re_calculate(rolls_live, results, False)
        game.total_score = sum(results)
        game.save()

        context = {'name': game.player, 'form': form, 'game_id': game.id, 'madeRolls': recordedFrames, 'results': results}
        return render(request, 'bowling/add_roll.html', context)

    def post(self, request, game_id):
        form = FrameForm(request.POST)
        game = get_object_or_404(Game, id=game_id)
        frames_passed = [[x.attempt1,x.attempt2,x.attempt3] for x in game.frames.all()]

        print len(frames_passed)

        if form.is_valid() and len(frames_passed) < 9:
            attempt1 = form.cleaned_data['attempt1']
            attempt2 = form.cleaned_data['attempt2']
            attempt3 = form.cleaned_data['attempt3']
            totalScore = int(attempt1)+int(attempt2)+int(attempt3)
            game.frames.create(attempt1=attempt1, attempt2=attempt2, attempt3=attempt3, total_score_in_frame=totalScore)
        elif len(frames_passed) == 9:
            attempt1 = form.cleaned_data['attempt1']
            attempt2 = form.cleaned_data['attempt2']
            attempt3 = form.cleaned_data['attempt3']
            totalScore = int(attempt1)+int(attempt2)+int(attempt3)
            game.frames.create(attempt1=attempt1, attempt2=attempt2, attempt3=attempt3, total_score_in_frame=totalScore)
            game.end_date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
            game.save()
        else:
            return HttpResponseRedirect(reverse('bowling:add_roll', args=(game_id,)))
        return HttpResponseRedirect(reverse('bowling:add_roll', args=(game_id,)))

def total_score(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    template = 'bowling/total_score.html'
    frame_results = [[x.attempt1, x.attempt2, x.attempt3] for x in game.frames.all()]
    results = []
    results = re_calculate(frame_results[:10], results, False)
    #in case of un handled post requests after the 10 frames are played
    if len(frame_results) > 10:
        game.total_score = sum(results[:10])
        game.save()

    time_played = seconds_to_minutes((game.end_date - game.start_date).seconds)

    context = {'game':game, 'results': results, 'total': game.total_score, 'start_date': game.start_date, 'end_date': game.end_date, 'time_played': time_played['time_played']}
    return render(request, template, context)


class BowlingAPI(APIView):

    renderer_classes = (JSONRenderer,)

    def get(self, request):
        games = Frame.objects.select_related('game').order_by('id')

        games_dict = OrderedDict()
        for game in games:
            print game.game.total_score,game.game.player
            games_dict[game.id] = {"attempt1": game.attempt1, "attempt2": game.attempt2, "attempt3": game.attempt3, "total_score_in_frame": game.total_score_in_frame, "game{}".format(game.game.id): {"player":game.game.player, "total_score": game.game.total_score}}
        return Response(games_dict)
