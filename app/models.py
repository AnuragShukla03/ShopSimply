from django.db import models

# Create your models here.

class SuperUser(models.Model):
    UserName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)


class Customer(models.Model):
    Name = models.TextField(max_length=50) 
    Contact = models.BigIntegerField()
    Amount =models.IntegerField()
    Date = models.TextField(max_length=50)
    
    Weight = models.FloatField()
    Rate = models.FloatField()
    Description = models.TextField(max_length=100)


    