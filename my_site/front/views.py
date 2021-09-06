from django import template
from django.http import HttpResponse, Http404
# Template 
from django.template import Context
from django.template.loader import get_template
# Render shortcut
from django.shortcuts import render
# Date
import datetime 
# OS
import os 
#Models
from .models import Book
# Forms
from .forms import ContactForm
# Redirect
from django.http import HttpResponseRedirect
# Mail
from django.core.mail import send_mail
# Get info about request objet 
def get_info(request):
    print('Request path =>',request.path)
    print('Request path =>',request.get_host())
    print('Request path =>',request.get_full_path())
    #print('Request Meta =>',request.META)
    print('META')
    meta = request.META
    for key in meta:
        print(key,':',meta[key])

def hello(request):
    now = datetime.datetime.now()
    get_info(request)
    # Replace by render_to_response
    #
    # Get the template
    #template = get_template('current_date_time.html')
    # Set the context
    #context = Context({'time':now})
    
    #html = template.render({'time':now})
    #return HttpResponse(html)
    #
    return render(request,'front/hello.html',{'time':now})

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

def search_form(request):
    return render(request,'front/search_form.html')


def search(request):
    print('Search  ==>')
    print('GET =>',request.GET)
    print('POST =>',request.POST)
    error = []

    if 'q' in request.GET:
        q = request.GET['q']
        # Check is q is empy
        if not q:
            error.append('Serach term is empty')
        elif len(q) > 5:
            error.append('Search term too long')
        else:
            
            books = Book.objects.filter(title__icontains=q)
            return render(request,'front/search_results.html',{
            'books':books,
            'q':q
            })  
    # Fallback options
    return render(request,'front/search_form.html',{
        'error':error
    })

    '''
    try:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        print('Bool q=>',bool(request.GET['q']))
        print('Books ==>',books)
        return render(request,'front/search_results.html',{
            'books':books,
            'q':q
            }) 
    except Exception as e:
        print('Erro =>',e)
        return render(request,'front/search_form.html',{
            'error':True
            }) 
    '''

def contact(request):
    print('Request ==>',request)
    print('Method ==>',request.method)
    # Check if GET or POST
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print('Form bound ==>',form.is_bound)
        print('Form valid ==>',form.is_valid())
        # Validathe the data
        if form.is_valid():
            my_data = form.cleaned_data
            print('Cleaned data ==>',my_data)
            send_mail(
                my_data['subject'],
                my_data['message'],
                my_data.get('email','norpely@test.com'),
                ['site@test.com']
                )
            return HttpResponseRedirect('/contact/thanks/')
        
    else:
        form = ContactForm()
    return render(request,'front/contact.html',{'form':form})

def contact_thanks(request):
    return HttpResponse('Thanks for your email!')