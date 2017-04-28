'''
Created on 21 Apr 2017

@author: shamil
'''
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login
from NewShkat05.models import User
from django.http import request
from django.http import HttpResponse
from django.contrib.auth.models import User
from NewShkat05.forms import RegisterForm

def login(request):
    title = 'login'
    
    username=request.POST['username']
    password=request.POST['password']
    user =auth.authenticate(username= username,password = password)
    
    return render_to_response('registration/login.html', locals(),RequestContext(request))

def logout(request):
    title ="Logout"
    message = " You are logout now , See you soon"
    return render_to_response('registration/logout.html',locals())

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
def register(request):
    form=RegisterForm().getAll()
    
    
    
    return render_to_response(("register.html", locals()))
def category (request):
    page_title = 'Категории'
    
    return render_to_response('category.html',locals())
