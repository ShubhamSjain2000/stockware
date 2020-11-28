from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User




class Indices(models.Model):

    
    
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    volume = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    dayhigh = models.IntegerField()
    daylow = models.IntegerField()
    
    nch = models.IntegerField()
    pch = models.IntegerField()
    fact = models.IntegerField()
  
    def __str__ (self):
        return self.name
    
    
    
    

class Traders(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Holdings(models.Model):
    holder = models.ForeignKey(Traders,on_delete =models.CASCADE)
    hold1 = models.CharField(max_length=100)
    quantity = models.IntegerField() 

class Scripts(models.Model):
    
    
    
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    volume = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    dayhigh = models.IntegerField()
    daylow = models.IntegerField()
    
    nch = models.IntegerField()
    pch = models.IntegerField()
    fact = models.IntegerField()

class GlobalIndices(models.Model): 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    volume = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    dayhigh = models.IntegerField()
    daylow = models.IntegerField()
    
    nch = models.IntegerField()
    pch = models.IntegerField()
    fact = models.IntegerField()

class Researches(models.Model):
    name = models.CharField(max_length=100)
    content= models.TextField()
    
  
    
    
    

    





