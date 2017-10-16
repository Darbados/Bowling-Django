from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import Frame, Game
from rest_framework import generics
from .serializers import GameSerializer
from .forms import NameForm, FrameForm
from .methods import *

class NameView(View):
    def get(self, request):
        form = NameForm()
        template = 'bowling/index.html'
        return render(request, template, {'form': form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            game = Game.objects.create(player=name)
        return HttpResponseRedirect(reverse('bowling:add_roll', args=(game.id,)))

class Add_Roll(View):
    def get(self, request, game_id):
        form = FrameForm()
        game = Game.objects.get(id=game_id)
        recordedFrames = game.frames.all()
        rolls_live = [[x.attempt1, x.attempt2, x.attempt3] for x in recordedFrames]
        results = [x.total_score_in_frame for x in recordedFrames]
        results = re_calculate(rolls_live, results, results[0])

        context = {'name': game.player, 'form': form, 'game_id': game.id, 'madeRolls': recordedFrames, 'results': results}
        return render(request, 'bowling/add_roll.html', context)

    def post(self, request, game_id):
        form = FrameForm(request.POST)
        game = get_object_or_404(Game, id=game_id)

        if form.is_valid():
            attempt1 = form.cleaned_data['attempt1']
            attempt2 = form.cleaned_data['attempt2']
            attempt3 = form.cleaned_data['attempt3']
            totalScore = int(attempt1)+int(attempt2)+int(attempt3)
            game.frames.create(attempt1=attempt1, attempt2=attempt2, attempt3=attempt3, total_score_in_frame=totalScore)
        return HttpResponseRedirect(reverse('bowling:add_roll', args=(game_id,)))

def total_score(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    template = 'bowling/total_score.html'
    frame_results = [[x.attempt1, x.attempt2, x.attempt3] for x in game.frames.all()]
    results = []
    results = re_calculate(frame_results, results, False)

    game.total_score = sum(results)
    context = {'game':game, 'results': results, 'total': game.total_score}
    return render(request, template, context)


class BowlingAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
