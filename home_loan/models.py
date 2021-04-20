from django.db import models

# Create your models here.
class HomeLoan(models.Model):
    amount= models.CharField(max_length=25)
    rate= models.CharField(max_length=25)
    month=models.CharField(max_length=20)


    #def __str__(self):
        #return self.amount"""
    
    

