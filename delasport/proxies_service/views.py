# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.http import HttpResponse
from models import *


def test(request):
    all_data = Source_Proxies.objects.using('tracker').all()
    template = "proxies_service/index.html"
    return render(request, template, {'context': all_data})


def getProxies(request):
    proxies = Proxy.objects.using('site').filter(is_active=1)
    return HttpResponse("<br>".join(["{}:{}".format(proxy.address,proxy.port) for proxy in proxies]))


def getParsers(request):
    python_parsers = (
        ('Ibcbet',7),
        ('Sbobet',15),
        ('William',18),
        ('Betsafe',20),
        ('TheGreek',32),
        ('Bwin',33),
        ('Unibet',34),
        ('Onexbet',48),
        ('TipSport',36),
        ('Expekt',37)
    )
    parsers_data = []
    for p in python_parsers:
        parser_data = Parsers.objects.using('tracker').filter(worker_key__contains=p[0])
        parsers_data.append(parser_data)

    proxies_list = Proxy.objects.using('site').filter(is_active=1)
    template = "proxies_service/parsers.html"
    return render(request, template, {'parsers': parsers_data, 'proxies': proxies_list})