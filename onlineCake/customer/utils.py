import json
from .models import *
from http.client import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import get_template, render_to_string
from django.template import Context
from datetime import datetime
from django.core.mail import send_mail,BadHeaderError
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
# from .sendsms import sending
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
		print("i have found my cart", cart)
	except:
		cart = {}
		print('CART:', cart)			
	
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
			'id':product.id,
			'product':{
				'id':product.id,
				'name':product.name,
				'price':product.priceAfterDiscount,
				'shippingFee':product.shippingFee,
				'imageURL':product.image.url,
			},
			'quantity':cart[i]["quantity"],
			
		}
		items.append(item)
	
	print({'cartItems':cartItems ,'order':order, 'items':items})			
	return {'cartItems':cartItems ,'order':order, 'items':items}

def cartData(request):
    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    order = cookieData['order']
    items = cookieData['items']
    return {'cartItems':cartItems ,'order':order, 'items':items}

	
def getOrder(request, data):
	
	customer = request.user.customer
	cookieData = cookieCart(request)
	items = cookieData['items']

	print("payment method: ",data['payMethod']);
	order = Order.objects.create(
		customer=customer,
		payMethod=data['payMethod'],
		complete=False,
		)
	print(items)
	for item in items:
		print("saving order")		
		product = Product.objects.get(id=item['id'])
		orderItem = OrderItem.objects.create(
			product=product,
			order=order,
			quantity=item['quantity'], # negative quantity = freebies
		)
		print("saving order")
		orderItem.save()
	return order


def sendEmail(request):
        
			subject = "Online uhy Cake Receipt" 
			email= form.cleaned_data['email'],  
			body= render_to_string("receipt.html",{'today':datetime.today()} )
			
        
			message = Mail(
				from_email='onlinebakery5@gmail.com',
				to_emails=form.cleaned_data['email'],
				subject='Cake Receipt',
				html_content=body
    )
			try:
				sg = SendGridAPIClient('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')
				sg.content_subtype = "html"
				response = sg.send(message)
				print(response.status_code)
				print(response.body)
				print(response.headers)
			except Exception as e:
				print(str(e))
