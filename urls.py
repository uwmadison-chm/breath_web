from django.conf.urls.defaults import *

from django.contrib import admin
#admin.autodiscover()

from timing import views

urlpatterns = patterns('',
    (r'^$', views.base),
    (r'login/', views.login),
    (r'instructions/', views.instructions),
    (r'practice/', views.practice),
    (r'run/', views.run),
    (r'submit/', views.submit),
)
