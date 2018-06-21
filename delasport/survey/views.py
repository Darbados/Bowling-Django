from django.shortcuts import render, redirect
from models import Survey


def index(request):
    latest_survey = Survey.objects.filter(status=Survey.SURVEY_STATUS_CREATED).order_by('-created_at')[0]
    latest_survey.status = Survey.SURVEY_STATUS_SENT
    latest_survey.save()

    return redirect('survey:survey', latest_survey.unique_value)


def survey(request, unique_value):
    survey = Survey.objects.get(unique_value=unique_value)
    survey.status = Survey.SURVEY_STATUS_COMPLETED
    survey.save()

    template = 'survey/survey.html'

    data = {
        'survey': survey
    }

    return render(request, template, data)
