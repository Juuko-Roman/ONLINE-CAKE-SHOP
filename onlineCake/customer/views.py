from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.

from django.http import HttpResponse

def index(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={'products':products,'categories':categories}
    return render(request, 'index.html',context)

def my_cart(request):  

    return render(request, 'my_cart.html')    

def category(request):
    products=Product.objects.filter(category=1)    
    categories=Category.objects.all()
    categToDisplay=Category.objects.filter(id=1)
    context={'products':products,'categories':categories,'categ':categToDisplay}      
    return render(request, 'category.html',context)

def order_details(request):
    context={}
    return render(request, 'order_details.html',context)

def product_details(request):
    context={}
    return render(request, 'product_details.html',context)

def track_order(request):
    context={}
    return render(request, 'track_order.html',context)

def track_orders(request):
    context={}
    return render(request, 'track_orders.html',context)            