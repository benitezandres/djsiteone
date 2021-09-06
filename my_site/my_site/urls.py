"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# My site views
from django.conf.urls import url
# Import for views
from front import views
# Settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello/$',views.hello),
    url(r'^time/$',views.time),
    url(r'^future/(\d{1,2})/$',views.future_time),
    url(r'^timef/(\d{1,2})$',views.timef),
    #url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search),
    url(r'^contact/$',views.contact),
    url(r'^contact/thanks/$',views.contact_thanks),
    url(r'^report/$',views.report_year),
    url(r'^report/(\d{4})/$',views.report_year),
    url(r'^report/(\d{4})/(\d{1,2})/$',views.report_year_month),
    url(r'^$',views.hello),
    
]

# Degun info to alter URL
if settings.DEBUG:
    #urlpatterns+= [url(r'^debuginfo$',views.debug),]
    pass
