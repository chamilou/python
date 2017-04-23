'''
Created on 21 Apr 2017

@author: shamil
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def welcome_page (request):
    page_title = 'Шкатулка'
    
    return render_to_response('index.html',locals())
def contact_me(request):
    page_title = "Обратная связь"
    tel ='мой тел:'
    tel_mob ='мой тел(мобильный):'
    email='мой е-мейл:'
    address= 'мой адрес:'
    
    return render_to_response('contact_me.html',locals())
def aboutUs (request):
    page_title = 'Про нас'
    
    return render_to_response('aboutUS.html',locals())
def category (request):
    page_title = 'Категории'
    
    return render_to_response('category.html',locals())
