'''
Created on 21 Apr 2017

@author: shamil
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def welcome_page (request):
    page_title = 'Шкатулка'
    
    return render_to_response('index.html',locals())