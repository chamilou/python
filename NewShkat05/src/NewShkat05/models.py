'''
Created on 23 Apr 2017

@author: shamil
'''

from django.db import models
from django.db.models import permalink
from django.contrib.admin.utils import help_text_for_field


class User(models.Model):
    name= models.CharField(max_length=30)
    
    email =models.EmailField(max_length=30)
    
    class Admin:
        pass

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length =50)
    slug= models.SlugField(max_length=50, unique =True,
                           help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords =models.CharField('Meta Keywords',max_length=255,
                                    help_text =' Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField('Meta Description', max_length =255,
                                        help_text='Content for description meta tag') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Category'
    def __str__(self):
        return u'%s' % (self.name)
     
    def get_absolute_url(self):
        return ('catalogue.category', (),{ 'Category_slug': self.slug})
class SUB_Category(models.Model):
    name = models.CharField(max_length =50)
    slug= models.SlugField(max_length=50, unique =True,
                           help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords =models.CharField('Meta Keywords',max_length=255,
                                    help_text =' Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField('Meta Description', max_length =255,
                                        help_text='Content for description meta tag') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    class Meta:
        db_table='sub_categories'
        ordering = ['-created_at']
        verbose_name_plural = 'SUB_Category'
    def __str__(self):
        return u'%s' % (self.name)
     
    def get_absolute_url(self):
        return ('catalogue.sub_category', (),{ 'Category_slug': self.slug})

    
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique = True,
                            help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.00)
    image = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField('Description')
    meta_keywords = models.CharField(max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255,
                                help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
    
    def __str__(self):
        return (self.name)
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_product', (), { 'product_slug': self.slug })
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
    