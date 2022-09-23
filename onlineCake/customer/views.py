from itertools import product
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

    try:
        cart=json.loads(request.COOKIES['cart'])
    except:
        cart={}

 
    items=[]
    order={'getCartTotal':0,'getCartItems':0}
    cartItems=order['getCartItems']

    for i in cart:
        cartItems += cart[i]["quantity"]
        product=Product.objects.get(id=i)
        total=(product.price*cart[i]["quantity"])

        order['getCartTotal']+=total
        order['getCartItems']+=cart[i]["quantity"]

        item={
            'product':{
                'id':product.id,
                'name':product.name,
                'price':product.price,
                'imageURL':product.image.url,
            },
            'quantity':cart[i]["quantity"],
            'getTotal':total
        }
        items.append(item)
    print(item['product'].get('imageURL'))
    context={'categories':categories,'items':items,'order':order,'cartItems':cartItems}        
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

# def UpdateItem(request):
#     data=json.loads(request.body)
#     productId=data['productId']
#     print(productId)
#     return JsonResponse('item was added', safe=False)    