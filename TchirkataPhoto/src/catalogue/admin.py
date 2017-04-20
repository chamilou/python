from django.contrib import admin
from catalogue.models import Category,Product, SUB_Category
from catalogue.forms import ProductAdminForm
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display=('name','price','old_price','created_at','updated_at',)
    list_display_links= ('name',)
    list_per_page=50
    ordering= ['-created_at']
    search_fields=['name','description','meta_keywords','meta_decription']
    exclude=('created_at', 'updated_at',)
    prepopulated_fields= {'slug': ('name',)}
class SUB_CategorieAdmin(admin.ModelAdmin):
    list_display=('name','created_at','updated_at',)
    list_display_links=('name',)
    list_per_page = 20
    ordering=['name']
    search_fields =['name','description','meta_keywords', 'meta_description']
    exclude =('created_at','updated_at',)
    prepopulated_fields = {'slug':  ('name',)}

class CategorieAdmin(admin.ModelAdmin):
    list_display=('name','created_at','updated_at',)
    list_display_links=('name',)
    list_per_page = 20
    ordering=['name']
    search_fields =['name','description','meta_keywords', 'meta_description']
    exclude =('created_at','updated_at',)
    prepopulated_fields = {'slug':  ('name',)}
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategorieAdmin)
admin.site.register(SUB_Category,SUB_CategorieAdmin)