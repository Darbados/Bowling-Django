# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Source_Proxies

def test(request):
    all_data = Source_Proxies.objects.using('proxies_service').all()
    template = "proxies_service/index.html"
    return render(request, template, {'context': all_data})
