from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from timing import views

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^$', views.welcome_consent),
    (r'^login$', views.login),
    (r'^demographics$', views.demographics),
    (r'^instructions$', views.instructions),
    (r'^practice$', views.practice),
    (r'^run_task$', views.run_task),
    (r'^thanks$', views.thanks),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root' : settings.PUBLIC_DIR})
    )