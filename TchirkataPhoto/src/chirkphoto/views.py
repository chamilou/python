from calendar import Calendar
import datetime

from django.contrib import auth
from django.db.models import Q
from django.forms import *
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response,get_object_or_404
from django.template.context import RequestContext
from django.utils import timezone

from catalogue.models import Product
from chirkphoto.forme import *

from chirkphoto.models import User



def home(request):
        salut ={1,2,3,4,5}
        now = timezone.now()
        doc ="Hi there MASMISCH"
        return render_to_response('index.html',locals())
#def search(request):
 #   query= request.GET.get('q','')
def main_page(request):
    now = timezone.now()
    
    return render_to_response('about_page.html',locals())

def register(request):
    
    title= ("Registration")
   
    if request.method == 'POST':
        form = RegistrationForm(request.POST) 
        if form.is_valid():
            user = User.objects.create(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'])
            
            return HttpResponseRedirect('/main_page')
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'form': form})
     
    return render_to_response('registration/register.html',locals(),context_instance= RequestContext(request))
def login(request):
    title = 'login'
    username=request.POST['username']
    password=request.POST['password']
    user =auth.authenticate(username= username,password = password)
    
    return render_to_response('registration/login.html', locals(),RequestContext(request))

def logout(request):
    
    return render_to_response('logout.html')
def myName(request):
    if request.method == 'POST':
        form = forms.NameClass(request.POST) 
        if form.is_valid():
            myName = Form.objects.get()
            
            return HttpResponseRedirect('templates/success.html/')
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'form': form})
     
    return render_to_response('test.html', locals())

def contactMe(request):
    title ='ContactMe'
    subject=''
    if request.method=='POST':
        forma= ContactMe(request.POST)
        if forma.is_valid():
            
            return HttpResponseRedirect('about_page.html')
    else: 
        forma=ContactMe()
        
        variables=RequestContext(request,{'forma':forma})
    
    
    return render_to_response('contactMe.html',locals(),RequestContext(request))
    
    

# Create your views here.
