from django.db import models
from django.contrib.auth.models import User

# Create your models here.




    
class MoreDetails(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    gender=models.CharField( max_length=50)
    telephone=models.CharField( max_length=50)
    location=models.TextField( max_length=50)
    

 