from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.conf import settings
from .views import (index, fabbricato)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

__author__ = 'sergio'

urlpatterns = patterns('fabbricati.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^fabbricato/(?P<id_fab>\w+)$', 'fabbricato', name='fabbricato'),
                       url(r'^ubicazione/(?P<id_fab>\w+)$', 'ubicazione', name='ubicazione'),
                       url(r'^elementi_catastali/(?P<id_fab>\w+)$', 'elementi_catastali', name='elementi_catastali'),
                       url(r'^riferimenti_temporali/(?P<id_fab>\w+)$', 'riferimenti_temporali', name='riferimenti_temporali'),
                       url(r'^riferimentiyuppies/(?P<id_fab>\w+)$', 'riferimentiyuppies', name='riferimentiyuppies'),
                       url(r'^caratteristichetecniche/(?P<id_fab>\w+)$', 'caratteristichetecniche', name='caratteristichetecniche'),
                       url(r'^datimetrici/(?P<id_fab>\w+)$', 'datimetrici', name='datimetrici'),
                       url(r'^altrielementicostruttivi/(?P<id_fab>\w+)$', 'altrielementicostruttivi', name='altrielementicostruttivi'),
                       )

#debug

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += \
        patterns('',
                 (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                     'document_root': settings.MEDIA_ROOT}))