from django.conf.urls import patterns, url
from django.conf import settings
from .views import (index,)

__author__ = 'sergio'

urlpatterns = patterns('fabbricati.views',
                       url(r'^$', 'index', name='index'),

                       )