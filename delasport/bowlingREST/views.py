from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import Game
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GameSerializer
from .forms import NameForm
from .methods import re_calculate

from .forms import NameForm


class NameView(View):
    def get(self, request):
        form = NameForm()
        template = 'bowlingREST/index.html'
        return render(request, template, {'form': form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            game = Game.objects.create(player=name)
        return HttpResponseRedirect(reverse('bowlingREST:add_roll', args=(game.id,)))


class Add_Roll(View):
    def get(self, request, game_id):
        game = get_object_or_404(Game, id=game_id)
        template = 'bowlingREST/add_roll.html'
        total_score_visible = ('hidden' if game.counterFrames < 21 else '')
        controller_form = ('' if game.counterFrames < 21 else 'hidden')
        context = {'game_id': game_id, 'player': game.player, 'counter': game.counterFrames, 'visibility': total_score_visible, 'control_form': controller_form}
        return render(request, template, context)

def total_score(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    rolls = [eval('game.roll' + str(x)) for x in range(1,22)]
    template = 'bowlingREST/total_score.html'
    results_obj = []

    for x in [x*2 for x in range(9)]:
        results_obj.append({'roll1': rolls[x], 'roll2': rolls[x+1]})
    results_obj.append({'roll1': rolls[18], 'roll2': rolls[19], 'roll3': rolls[20]})

    results_obj = re_calculate(results_obj)
    maximums = [frame['total'] for frame in results_obj]
    minimums = [frame['total'] for frame in results_obj]

    highest = results_obj.index(results_obj[maximums.index(max(maximums))])
    lowest = results_obj.index(results_obj[minimums.index(min(minimums))])

    print highest,lowest

    results_obj[highest]['highest'] = 'success'
    results_obj[highest]['top'] = 'TOP'
    results_obj[lowest]['lowest'] = 'danger'
    results_obj[lowest]['poor'] = 'LOWEST'

    headers = ['Frame #', 'Roll 1', 'Roll 2', 'Roll 3', 'Strike', 'Spare', 'Result', 'Highest', 'Lowest']
    total = sum([frame['total'] for frame in results_obj])
    game.total_score = total
    game.save()
    context = {'frames': results_obj, 'total': total, 'headers': headers}

    return render(request, template, context)

class Add_RollAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
