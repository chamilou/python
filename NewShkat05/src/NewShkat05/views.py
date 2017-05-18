'''
Created on 21 Apr 2017

@author: shamil
'''
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import request
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect

from NewShkat05.forme import ContactForm, RegisterForm
from NewShkat05.models import Category,Product


@csrf_protect
def login(request):
    title = 'Вход'
    header="Header in Login"
    username=request.POST['username']
    password=request.POST['password']
    user =auth.authenticate(username= username,password = password)
    
    return render_to_response('registration/login.html', locals(),RequestContext(request))

def logout(request):
    title ="Logout"
    message = " You are logout now , See you soon"
    return render_to_response('registration/logout.html',locals())

def index (request):
    page_title = 'Шкатулка'
    
    
    return render_to_response('index.html',locals())
def contact_me(request):
    page_title= "Связатсья с нами"
    contact= ''
    
    form = ContactForm()
    
    if request.method == 'POST':
        contact= request.POST.get('contact_address: ','')+" and phone : "+request.POST.get('mob_Telephone')
        
        
    
    return render_to_response('contact_me.html',locals(),RequestContext(request))
def aboutUs (request):
    title = 'Про нас'
    
    return render_to_response('aboutUS.html',locals())
def register(request):
    
    reg = RegisterForm()
    
    
    return render_to_response('register.html',locals())
    
def product(request):
    page_title= "produkt"
    
    prod=Product.objects.all()
    
    
    return render_to_response('product.html',locals())   
def category (request):
    page_title = 'Категории'

    cat = Category.objects.all()
    
    return render_to_response('category.html',locals())
