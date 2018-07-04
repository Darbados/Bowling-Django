from django.shortcuts import render, redirect, reverse
from models import Survey
from survey.forms import SurveyForm


def index(request):
    template = 'survey/survey.html'
    form = SurveyForm()
    data = {
        'form': form,
    }

    return render(request, template, data)

