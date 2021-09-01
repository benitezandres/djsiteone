from django import template
from django.http import HttpResponse, Http404
# Template 
from django.template import Template, Context
from django.template.loader import get_template
import datetime 

import os 

def hello(request):
    template = get_template('current_date_time.html')

    return HttpResponse('Hi!')

def time(request):
    now = datetime.datetime.now()
    name = 'Andres'
    html ='The time now is {0}'.format(now)
    #html = "<h1>Hi %s, the time now is %s </h1>" % (name, now)
    return HttpResponse(html)

def future_time(request,offset):
    print('Offset=>',offset,type(offset))
    
    try:
        offset = int(offset)
    except ValueError:
        return Http404()
    #assert False
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = 'The future time is {0}'.format(dt)
    return HttpResponse(html)

def timef(request,offset):
    print(request,offset,type(offset))
    print('Path =>',os.path.dirname(__file__))
    offset = int(offset)
    date = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<h1>The time in the furete is {0}/{1}/{2}:{3}'.format(date.year,date.month,date.day,date.hour)
    return HttpResponse(html)