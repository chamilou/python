#from shop import urls as shop_urls
from django.conf.urls import patterns, include, url
from django.contrib import admin
from chirkphoto.views import *
from django.contrib.auth.views import login, logout
import os.path

from catalogue.views import shoping, show_product, index, show_category
from django.conf.urls.static import static
from TchirkataPhoto import settings


site_media = os.path.join(
     os.path.dirname(__file__), 'site_media')
     
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TchirkataPhoto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^date_time/', home),
    url(r'^main_page/', home),
    url(r'^shoping_page/', shoping),
    
    url(r'^login/$',login),
    url(r'^logout/$',logout),
    url(r'^$',home),
    url(r'^register/$',register),
    url(r'^myName/$',myName),
    url(r'^contactMe/$',contactMe),
    #url(r'^catalogue/', include(catalogue_urls)),
    

    url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
       { 'document_root': site_media }),
)
