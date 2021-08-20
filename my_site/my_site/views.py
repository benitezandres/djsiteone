from django.http import HttpResponse, Http404
import datetime 

def hello(request):
    return HttpResponse('Hi!')

def time(request):
    now = datetime.datetime.now()
    html ='The time now is {0}'.format(now)
    return HttpResponse(html)

def future_time(request,offset):
    print('Offset=>',offset,type(offset))
    try:
        offset = int(offset)
    except ValueError:
        return Http404()
    
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = 'The future time is {0}'.format(dt)
    return HttpResponse(html)