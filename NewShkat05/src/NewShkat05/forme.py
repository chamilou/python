'''
Created on 26 Apr 2017

@author: shamil
'''
from django import forms

class RegisterForm(forms.Form):
    username= forms.CharField(label="Username")
    