# from http.client import HttpResponse
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
	return render (request, "cat.html")

def transaction(request):
	return render (request, "transaction.html")
	
def pdtlist(request):
	return render (request, "transaction.html")

def customer(request):
	return render (request, "customer.html")

def orders(request):
	return render (request, "orders.html")
	
def reports(request):
	return render (request, "reports.html")

def dashboard(request):
	if request.user.is_authenticated:
		return render(request, "dashboardhome.html")
	else:
		return redirect('/accounts/Alogin/')

def addpdt(request):
	return render (request, "addpdt.html")