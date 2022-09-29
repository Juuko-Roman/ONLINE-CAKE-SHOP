from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    
    username= models.CharField(max_length=50)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    company= models.CharField(max_length=50) 
    regDate=models.DateField (default=datetime.datetime.today)
    def __str__(self):
        return self.username



    
class MoreDetails(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    gender=models.CharField( max_length=50)
    telephone=models.CharField( max_length=50)
    location=models.TextField( max_length=50)
    

 