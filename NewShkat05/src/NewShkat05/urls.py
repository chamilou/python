from django.conf.urls import patterns, include, url
from django.contrib import admin
from NewShkat05.views import *
import django.contrib.auth as auth_log

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewShkat05.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$',welcome_page),
    url('^contact_me$',contact_me),
     url(r'^login/$', login),
    url(r'^logout/$', auth_log.logout, name='logout'),
    url('^aboutUs$',aboutUs),
    url('^category$',category),

    url(r'^admin/', include(admin.site.urls)),
)
