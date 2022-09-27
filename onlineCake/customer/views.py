from http.client import HTTPResponse

from multiprocessing import context

from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from .utils import *

# Create your views here.

def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    
    products=Product.objects.all()
    categories=Category.objects.all()
    context={'products':products,'categories':categories,'cartItems':cartItems}
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
        total=(product.priceAfterDiscount*cart[i]["quantity"]+product.shippingFee)

        order['getCartTotal']+=total
        order['getCartItems']+=cart[i]["quantity"]

        item={
            'product':{
                'id':product.id,
                'name':product.name,
                'price':product.priceAfterDiscount,
                'shippingFee':product.shippingFee,
                'imageURL':product.image.url,
            },
            'quantity':cart[i]["quantity"],
            'getTotal':total
        }
        items.append(item)

    context={'categories':categories,'items':items,'order':order,'cartItems':cartItems}        
    return render(request, 'my_cart.html', context)    

def category(request,id):
    print(id)
    data = cartData(request)
    cartItems = data['cartItems']
    
    
    products=Product.objects.filter(category=id)    
    categories=Category.objects.all()
    categToDisplay=Category.objects.filter(id=id)
    context={'products':products,'categories':categories,'categ':categToDisplay,'cartItems':cartItems}      
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
        total=(product.priceAfterDiscount*cart[i]["quantity"]+product.shippingFee)

        order['getCartTotal']+=total
        order['getCartItems']+=cart[i]["quantity"]

        item={
            'product':{
                'id':product.id,
                'name':product.name,
                'price':product.priceAfterDiscount,
                'shippingFee':product.shippingFee,
                'imageURL':product.image.url,
            },
            'quantity':cart[i]["quantity"],
            'getTotal':total
        }
        items.append(item)

    context={'categories':categories,'items':items,'order':order,'cartItems':cartItems}         
    return render(request, 'checkout.html',context)  

def likeIncrease(request):
    data = json.loads(request.body)
    productId = data['productId']
    
    product = Product.objects.get(id=productId)
    product.likes+=1;

    newLikes=product.likes
    product.save()

    return JsonResponse(newLikes, safe=False)

def likeDecrease(request):
    data = json.loads(request.body)
    productId = data['productId']
    
    product = Product.objects.get(id=productId)
    product.likes-=1;

    newLikes=product.likes
    product.save()

    return JsonResponse(newLikes, safe=False)    

# def UpdateItem(request):
#     data=json.loads(request.body)
#     productId=data['productId']
#     print(productId)
#     return JsonResponse('item was added', safe=False)    

def searchResults(request):
    searchWord=request.POST['search']    
    data = cartData(request)
    cartItems = data['cartItems']
    
    products=Product.objects.filter(name__icontains=searchWord) 
    categories=Category.objects.all()
    context={'products':products,'categories':categories,'cartItems':cartItems, 'searchWord':searchWord}
    return render(request, 'searchResults.html',context)

def processOrder(request):
	# transaction_id = datetime.datetime.now().timestamp()
	# data = json.loads(request.body)

	# order = order(request, data)

	# total = float(data['form']['total'])
	# order.transaction_id = transaction_id

	# if total == order.get_cart_total:
	# 	order.complete = True
	# order.save()

	# ShippingDetails.objects.create(
	# customer=customer,
	# order=order,
	# Address=data['shipping']['SAddress'],
	# City=data['shipping']['SCity'],
	# State=data['shipping']['SState'],
	# PinCode=data['shipping']['SPin'],
	# 	)

	return JsonResponse('Payment submitted..', safe=False)    
