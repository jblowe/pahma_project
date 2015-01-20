__author__ = 'jblowe'

from django.conf.urls import patterns, url
from locviewer import views

urlpatterns = patterns('',
                       url(r'^$', views.locations, name='locations'),
                       url(r'^(?P<count>[\d]+)/$', views.locations, name='locations'),
                       )