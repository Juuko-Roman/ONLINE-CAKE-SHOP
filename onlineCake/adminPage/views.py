# from http.client import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import get_template, render_to_string
from django.template import Context
from datetime import datetime
from django.core.mail import send_mail,BadHeaderError
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from customer.models import *
# from .sendsms import sending
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# Create your views here.
def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
        
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
      
	form = ContactForm()
	return render(request, "index.html", {'form':form})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
        
			subject = "Online Cake Receipt" 
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
      
	form = ContactForm()
	return render(request, "index.html", {'form':form})


# def index(request):
#     if request.method=='POST':
#        form=ContactForm(request.POST)
       
#        if form.is_valid():
#             print('the form is valid')

#             subject=form.cleaned_data['subject']
#             email =form.cleaned_data['email']
#             content =form.cleaned_data['content']

#             html =render_to_string('Email/contactform.html',{
#                 'subject': subject,
#                 'email': email,
#                 'content': content
#             })
#             send_mail('the subject', 'hello World', 'onlinebakery5@gmail.com',['waterasheilah@gmail.com'],html_message=html)  
#             return redirect('index')

#     else:
#         form=ContactForm()

#     return render(request, 'index.html',{ 
#         'form': form 
#     })

def cat(request):
	categories=Category.objects.all()
	products=[]
	
	for category in categories:
		products.append(Product.objects.filter(category=category.id))
		
	context={'categories':categories,'products':products}
	return render (request, "cat.html",context)

def transaction(request):
	orders=Order.objects.all()
	context={'orders':orders}
	return render (request, "transaction.html",context)
	
def pdtlist(request):
	products=Product.objects.all()
	context={'products':products}
	return render (request, "pdtlist.html",context)

def customer(request):
	customers=Customer.objects.all()
	context={'customers':customers}
	return render (request, "customer.html",context)

def orders(request):
	orders=Order.objects.all()
	context={'orders':orders}
	return render (request, "orders.html",context)
	
def reports(request):
	context={}
	return render (request, "reports.html",context)

def viewOrderDetails(request,id):
orderItems=OrderItem.objects.filter(order=id)
	context={'orderItems':orderItems}
	return render (request, "reports.html",context)

def changeOrderStatus(request):
	context={}
	return render (request, "reports.html",context)


def deleteCategory(request,id):
member = Members.objects.get(id=id)
  member.delete()
	context={}
	return render (request, "reports.html",context)


def editCategory(request,id):
mymember = Members.objects.get(id=id)
  context = {
    'mymember': mymember}
	return render (request, "reports.html",context)

def editCategoryRec(request,id):
first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
return render (request, "reports.html",context)


def editProductRec(request,id):
first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
return render (request, "reports.html",context)


def deleteProduct(request,id):
    member = Members.objects.get(id=id)
  member.delete()
	context={}
	return render (request, "reports.html",context)

def dashboard(request):
	orders=Order.objects.all()
	orderTotal=0
	for order in orders:
		orderTotal+=1

	products=Product.objects.all()
	productTotal=0
	for product in products:
		productTotal+=1		

	orderItems=OrderItem.objects.all()
	totalSales=0
	for orderItem in orderItems:
		totalSales+=orderItem.quantity*orderItem.product.priceAfterDiscount+orderItem.product.shippingFee
	
	context={'orderTotal':orderTotal,'productTotal':productTotal,'totalSales':totalSales,'date':datetime.datetime.today,'orders':orders}
	if request.user.is_authenticated:
		return render(request, "dashboardhome.html",context)
	else:
		return redirect('/accounts/Alogin/')

def addpdt(request):
     If request.method==POST:
         x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
     else:
	 return render (request, "addpdt.html")

def editProduct(request,id):
mymember = Members.objects.get(id=id)
  context = {
    'mymember': mymember,}
	
	return render (request, "reports.html",context)
