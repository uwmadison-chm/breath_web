from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from .timing import views

urlpatterns = patterns('',
    (r'^$', views.instructions),
    (r'^login/', views.login),
    (r'^run/', views.run),
    (r'^practice/', views.practice),
    (r'^submit/', views.submit),
    (r'^instructions/', views.instructions),
    (r'^admin/', include(admin.site.urls))
)
