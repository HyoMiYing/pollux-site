from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ptmstatus.models import PtmStatus

def main_site(request):
    data = PtmStatus.objects.using('data').all()
    template = loader.get_template('ptmstatus/index.html')
    context = {
        'data' : data,
    }
    return HttpResponse(template.render(context, request))