from multiprocessing import context
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# Create your views here.

def index(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={'products':products,'categories':categories}
    return render(request, 'index.html',context)

def my_cart(request):  
    categories=Category.objects.all()
    context={'categories':categories}        
    return render(request, 'my_cart.html', context)    

def category(request):
    products=Product.objects.filter(category=1)    
    categories=Category.objects.all()
    categToDisplay=Category.objects.filter(id=1)
    context={'products':products,'categories':categories,'categ':categToDisplay}      
    return render(request, 'category.html',context)

def order_details(request):
    categories=Category.objects.all()
    context={'categories':categories}     
    return render(request, 'order_details.html',context)

def product_details(request):
    categories=Category.objects.all()
    context={'categories':categories}     
    return render(request, 'product_details.html',context)

def track_order(request):
    categories=Category.objects.all()
    context={'categories':categories}     
    return render(request, 'track_order.html',context)

def track_orders(request):
    categories=Category.objects.all()
    context={'categories':categories}     
    return render(request, 'track_orders.html',context)   

def checkout(request):
    categories=Category.objects.all()
    context={'categories':categories}     
    return render(request, 'index.html',context)                

def UpdateItem(request):
    return JsonResponse('item was added', safe=False)    