from http.client import HTTPResponse

from multiprocessing import context

from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
import json
from .utils import *
from django.contrib.auth import logout

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
    data = cartData(request)
    cartItems = data['cartItems']    
    categories=Category.objects.all()

    if request.user.is_authenticated: 
        pass
    else:
        context={'categories':categories, 'cartItems':cartItems}        
        return redirect('/accounts/login/',context)     

    order=Order.objects.filter(customer=request.user.customer).only('id').all()
    orderItems=OrderItem.objects.filter(order__in=order)
    context={'categories':categories, 'cartItems':cartItems,'orderItems':orderItems}    
    
    return render(request, 'order_details.html',context)
    
def product_details(request):
    categories=Category.objects.all()
    context={'categories':categories}     
    return render(request, 'product_details.html',context)

def track_order(request,id):
    orderItems=OrderItem.objects.filter(id=id)
    
    order=Order.objects.filter(id=orderItems[0].order.id)
    print(order)
    if order[0].status=="Delivered":
        statusCheck=True
    else:
        statusCheck=False
    context={'orderItems':orderItems,'statusCheck':statusCheck}     
    return render(request, 'track_order.html',context)

def track_orders(request):
    categories=Category.objects.all()
    context={'categories':categories}     
    return render(request, 'track_orders.html',context)   

def checkout(request):
    categories=Category.objects.all()
    context={'categories':categories}         
    
    if request.user.is_authenticated: 
        pass
    else:    
         return redirect('/accounts/login/',context)    
    data = cartData(request)
    cartItems = data['cartItems']    
    
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
    
    print("id: ",request.user.customer)
    customer = request.user.customer
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    print(data['payMethod'])

    order = getOrder(request, data)

    order.transaction_id = transaction_id

    order.complete = True
    order.save()

    shipping=ShippingDetail.objects.create(
    customer=customer,
    order=order,
    Address=data['shipping']['address'],
    City=data['shipping']['city'],
    State=data['shipping']['state'],
    Pincode=data['shipping']['pinCode'],
        )
    
    shipping.save()
        
    return JsonResponse('Payment submitted..', safe=False)    
