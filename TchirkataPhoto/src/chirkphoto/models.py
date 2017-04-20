from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=30)
    
    email =models.EmailField(max_length=30)
    class Admin:
        pass

    def __str__(self):
        return self.name
    
class Test(models.Model):
    name=models.CharField(max_length=30)
    fname = models.CharField(max_length=50)
    webS = models.URLField(max_length=50)
    
    