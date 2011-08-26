from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from timing import views

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^(?P<slug>[A-Za-z0-9_]+)$', views.welcome_consent),
    (r'^(?P<slug>[A-Za-z0-9_]+)/background$', views.background),
    (r'^(?P<slug>[A-Za-z0-9_]+)/privacy$', views.privacy),
    (r'^(?P<slug>[A-Za-z0-9_]+)/login$', views.login),
    (r'^(?P<slug>[A-Za-z0-9_]+)/demographics$', views.demographics),
    (r'^(?P<slug>[A-Za-z0-9_]+)/instructions$', views.instructions),
    (r'^(?P<slug>[A-Za-z0-9_]+)/guided_practice$', views.guided_practice),
    (r'^(?P<slug>[A-Za-z0-9_]+)/practice$', views.practice),
    (r'^(?P<slug>[A-Za-z0-9_]+)/run_task$', views.run_task),
    (r'^(?P<slug>[A-Za-z0-9_]+)/thanks$', views.thanks),
    (r'^(?P<slug>[A-Za-z0-9_]+)/log/(?P<view_key>.*)$', views.log)
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root' : settings.PUBLIC_DIR})
    )