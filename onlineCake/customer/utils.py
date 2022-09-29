import json
from .models import *

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

	order = Order.objects.create(
		customer=customer,
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

