from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    
    username= models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    gender=models.CharField(max_length=6)
    location = models.CharField(max_length=100) 
    regDate=models.DateField (default=datetime.datetime.today)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=60)
    priceBeforeDiscount= models.IntegerField(default=0)
    priceAfterDiscount= models.IntegerField(default=0)
    shippingFee= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='customer/static/Assets/images/products/')
    likes=models.IntegerField(default=0)

class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    complete = models.BooleanField (default=False)
    

class ShippingDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Address  = models.CharField (max_length=50, default='', blank=True)
    State = models.CharField (max_length=50, default='', blank=True)
    City  = models.DateField (max_length=50, default='', blank=True)
    Pincode  = models.IntegerField ()    

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)