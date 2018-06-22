from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from models import Survey
from forms import RatingForm


def index(request):
    latest_survey = Survey.objects.filter(status=Survey.SURVEY_STATUS_CREATED).order_by('-created_at')[0]
    survey_unique_value = latest_survey.unique_value

    latest_survey.status = Survey.SURVEY_STATUS_SENT
    latest_survey.save()

    print "Debug"
    print survey_unique_value
    print "Debug"

    return redirect('survey:survey', survey_unique_value)


def survey(request, uv):
    if Survey.objects.get(unique_value=uv).status == Survey.SURVEY_STATUS_SENT:
        survey = Survey.objects.get(unique_value=uv)

        survey.status = Survey.SURVEY_STATUS_COMPLETED
        survey.save()

        template = 'survey/survey.html'

        data = {
            'survey': survey
        }

        return render(request, template, data)
    else:
        return render(request, 'survey/completed.html')


def form_view(request):
    template = 'survey/rating.html'
    form = RatingForm()

    data = {
        'form': form
    }

    return render(request, template, data)

def completed(request):
    template = 'survey/completed.html'

    return render(request, template)