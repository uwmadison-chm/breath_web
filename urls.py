from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'timing.views.instructions'),
    (r'^login/', 'timing.views.login'),
    (r'^run/', 'timing.views.run'),
    (r'^practice/', 'timing.views.practice'),
    (r'^submit/', 'timing.views.submit'),
    (r'^instructions/', 'timing.views.instructions'),
    (r'^admin/', include(admin.site.urls))
)
