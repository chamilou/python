from django.conf.urls import patterns, include, url
from django.contrib import admin
from NewShkat05.views import *
import django.contrib.auth as auth_log

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewShkat05.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$',index),
    url('^contact_me$',contact_me),
     #url(r'^login/$','django.contrib.auth.views.login', {'template_name': 'registration/login.html'}
     url(r'^login/$',login),
    url(r'^logout/$', auth_log.logout, name='logout'),
    url('^aboutUs$',aboutUs),
    url('^category$',category),

    url(r'^register/$', register),
    url(r'^product$', product),
    url(r'^success$', success),
    
    url(r'^admin/', include(admin.site.urls)),
    
)
