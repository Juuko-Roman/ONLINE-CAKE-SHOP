from contextvars import Context
from django.shortcuts import render, redirect
from customer.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . models import MoreDetails
from . models import Seller
from customer .utils import *

# Create your views here.

from django.http import HttpResponse

def login(request):
    data = cartData(request)
    cartItems = data['cartItems']    
    categories=Category.objects.all()
    context={'categories':categories,'cartItems':cartItems}       

    if request.user.is_authenticated: 
        return redirect('/checkout/',context)
    else:    

        if request.method== "POST":
            
            
            username=request.POST['name']
            password=request.POST['password']
            user=auth.authenticate(request,username=username,password=password)
            
            if user is not None:
                
                auth.login(request,user)
                return redirect('/checkout/') 
            else:
                
                messages.info(request,'invalid credentials') 
                return render(request, 'Customerlogin.html', context)  
        else:
            return render(request, 'Customerlogin.html', context)
        
def register(request):
    data = cartData(request)
    cartItems = data['cartItems']    
    categories=Category.objects.all()
    context={'categories':categories,'cartItems':cartItems}       
          
    if request.method== "POST":
        username=request.POST['name']
        email=request.POST['email']
        gender=request.POST['gender']
        telephone=request.POST['tel']
        location=request.POST['Location']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if (password1==password2):
            if Customer.objects.filter(username=username).exists():
                print("username taken")
            elif Customer.objects.filter(email=email).exists(): 
                print("email taken")
            else:
                user,created=Customer.objects.get_or_create(username=username,email=email,password=password1,gender=gender,phone=telephone,location=location)
                user.save()
                messages.info(request,'succesfully Registered') 
                getUser = Customer.objects.get(email=email)
                print(getUser)
                # moredetails = MoreDetails.objects.create(user=getUser,gender=gender,telephone=telephone,location=location)
                # moredetails.save()
        return redirect('/accounts/login/')     
    else:
        return render(request, 'register.html', context)  

def signout(request):

    logout(request)
    messages.info(request,'succesfully logged out') 
    return redirect('/accounts/login/') 

def Alogin(request):
    categories=Category.objects.all()
    context={'categories':categories}         
    if request.method== "POST":
           
        username=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(request,username=username,password=password)
            
        if user is not None:
                
            auth.login(request,user)
            return redirect('/AdiminDashboard/') 
        else:
                
            messages.info(request,'invalid credentials') 
            return render(request, 'login.html', context)  
             
    else:
        return render(request, 'login.html', context)
        
def Aregister(request):
    categories=Category.objects.all()
    context={'categories':categories}         
    if request.method== "POST":
        username=request.POST['name']
        email=request.POST['email']
        company=request.POST['company']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if (password1==password2):
            if Seller.objects.filter(username=username).exists():
                print("username taken")
            elif Seller.objects.filter(email=email).exists(): 
                print("email taken")
            else:
                user,created=Seller.objects.get_or_create(username=username,email=email,password=password1,company=company)
                user.save()
                getUser = Seller.objects.get(email=email)
                print(getUser)
                messages.info(request,'successfully registered') 
                
        return redirect('/accounts/Alogin/')     
        
    else:
        return render(request, 'Aregister.html', context)         
