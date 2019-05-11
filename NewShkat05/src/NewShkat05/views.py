'''
Created on 21 Apr 2017

@author: shamil
'''
from django.contrib import auth

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import request
from django.shortcuts import render_to_response,render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect

from NewShkat05.forme import ContactForm, RegisterForm
from NewShkat05.models import Category,Product
from django.utils.decorators import method_decorator


@csrf_protect
def login(request):
    title = 'Вход'
    password =username= ''
    
    if request.POST.get('username'):
        
        password=request.POST['password']
        username= request.POST['username']
        return render_to_response('success.html', locals())
        
    
   
    return render(request,'registration/login.html',{'title':title})
def logout(request):
    title ="Logout"
    message = " You are logout now , See you soon"
    return render_to_response(request,'registration/logout.html')

def index (request):
    title = 'Шкатулка'
    return render_to_response('index.html',locals())
def success (request):
    page_title = 'Шкатулка'    
    success= 'Success'
    return render_to_response('index.html',locals())
def contact_me(request):
    page_title= "Связатсья с нами"
    user = User
    contact= ''
    
    form = ContactForm()
    
    if request.method == 'POST':
        contact= request.POST.get('contact_address','') +" and phone : "+request.POST.get('mob_Telephone')
        
        
    
    return render_to_response('contact_me.html',locals(),RequestContext(request))
def aboutUs (request):
    title = 'Про нас'
    
    return render_to_response('aboutUS.html',locals())
def register(request):
    title= "Registraziya"
    username=password=''
    if request.method =='POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            new_user = User.objects.create_user(username, password)
            return render_to_response('index.html', locals())
        else: message='You have to enter valid data'
    else: 
        reg_form = RegisterForm()
    
    
    return render_to_response ('register.html',locals(),RequestContext(request))
    
def product(request):
    page_title= "produkt"
    
    prod=Product.objects.all()
    
    
    return render_to_response('product.html',locals())   
def category (request):
    page_title = 'Категории'

    cat = Category.objects.all()
    
    return render_to_response('category.html',locals())
