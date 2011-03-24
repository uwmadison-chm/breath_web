from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from timing import views

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^$', views.welcome_consent),
    (r'^background$', views.background),
    (r'^privacy$', views.privacy),
    (r'^login$', views.login),
    (r'^demographics$', views.demographics),
    (r'^instructions$', views.instructions),
    (r'^guided_practice$', views.guided_practice),
    (r'^practice$', views.practice),
    (r'^run_task$', views.run_task),
    (r'^thanks$', views.thanks),
    (r'^log/(?P<view_key>.*)$', views.log)
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root' : settings.PUBLIC_DIR})
    )