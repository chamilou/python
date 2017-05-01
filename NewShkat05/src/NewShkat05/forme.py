'''
Created on 26 Apr 2017

@author: shamil
'''
from django import forms


from NewShkat05.models import Product,Category,  SUB_Category

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model= Product
        
        def clean_price(self):
            if self.cleaned_data['price']<=0:
                raise forms.ValidationError('Price must be greater then zero')
            return self.cleaned_data['price']

class RegisterForm(forms.Form):
    pass
    #username= forms.CharField(label="Username", max_length=255)
    