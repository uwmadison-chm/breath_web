from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin

from timing import views

urlpatterns = patterns('',
    (r'^$', views.base),
    (r'login/', views.login),
    (r'instructions/', views.instructions),
    (r'practice/', views.practice),
    (r'run/', views.run),
    (r'submit/', views.submit),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root' : settings.PUBLIC_DIR})
    )