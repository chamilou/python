from django import forms

from catalogue.models import Product, Category

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model= Product
        
        def clean_price(self):
            if self.cleaned_data['price']<=0:
                raise forms.ValidationError('Price must be greater then zero')
            return self.cleaned_data['price']
        
#class CategoryAdminForm(forms.ModelForm):
#   class Meta:
#       model =Category
#          def clean_name(self):
#             return self.cleaned_data('name')
        
                