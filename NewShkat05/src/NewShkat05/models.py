'''
Created on 23 Apr 2017

@author: shamil
'''

from django.db import models


class User(models.Model):
    name= models.CharField(max_length=30)
    
    email =models.EmailField(max_length=30)
    class Admin:
        pass

    def __str__(self):
        return self.name