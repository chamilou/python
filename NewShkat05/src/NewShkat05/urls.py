from django.conf.urls import patterns, include, url
from django.contrib import admin
from NewShkat05.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewShkat05.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$',welcome_page),
    url('^$',contact_me),

    url(r'^admin/', include(admin.site.urls)),
)
