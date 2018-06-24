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
    polucheno = request.GET.get('pesho') or None

    data = {
        'form': form,
    }

    if polucheno is not None:
        data['polucheno'] = polucheno

    return render(request, template, data)


def all_surveys(request):
    template = 'survey/all.html'
    created_at = request.GET.get('created_at') or None
    status = request.GET.get('status') or None

    print("REQUEST GET")
    print(request.GET)
    print("REQUEST GET")

    sort_obj = {}

    if created_at is not None:
        if created_at == 'oldest':
            sort_obj['condition'] = 'created_at'
        elif created_at == 'newest':
            sort_obj['condition'] = '-created_at'
    elif status is not None:
        if status == 'asc':
            sort_obj['condition'] = 'status'
        elif status == 'desc':
            sort_obj['condition'] = '-status'

    if 'condition' in sort_obj:
        surveys = Survey.objects.order_by(sort_obj['condition'])
    else:
        surveys = Survey.objects.all()

    data = {
        'surveys': surveys
    }

    return render(request, template, data)


def completed(request):
    template = 'survey/completed.html'

    return render(request, template)