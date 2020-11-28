from django.db import models
from price.models import Indices



class Traders(models.Model):
    
    name = models.CharField(max_length=100)

    price = models.IntegerField()

