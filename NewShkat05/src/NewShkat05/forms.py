'''
Created on 26 Apr 2017

@author: shamil
'''
from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label="username", max_length=50)
    password = forms.PasswordInput(label = "password", max_length=100)
    