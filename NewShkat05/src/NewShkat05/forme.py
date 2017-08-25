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
    
    username= forms.CharField(label="Username", max_length=255)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput())
                                
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')
 
   
    def __str__(self):
        return self.username
    
    
class ContactForm(forms.Form):
    mob_Telephone = forms.CharField(label="mobPhone", max_length=255, required=False)

    contact_email= forms.EmailField(label="your_email", required = True )
    
    contact_address= forms.CharField(label ="address")
    your_message= forms.CharField(widget =forms.Textarea)
    
    
    