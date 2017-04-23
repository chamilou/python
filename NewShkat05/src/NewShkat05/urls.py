from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from NewShkat05.views import *
from django.contrib.auth import logout, login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewShkat05.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$',welcome_page),
    url('^contact_me$',contact_me),
    url('^login$',login),
    url('^logout$',logout),
    url('^aboutUs$',aboutUs),
    url('^category$',category),

    url(r'^admin/', include(admin.site.urls)),
)
