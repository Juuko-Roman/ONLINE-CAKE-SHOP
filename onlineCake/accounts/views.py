from contextvars import Context
from django.shortcuts import render, redirect
from customer.models import *
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . models import MoreDetails

# Create your views here.

from django.http import HttpResponse

def login(request):
    categories=Category.objects.all()
    context={'categories':categories}         
    if request.method== "POST":
        
        
        # email=request.POST['email']
        # password=request.POST['password']
        # user=auth.authenticate(request,email=email,password=password)
         
        # if user is not None:
            
        #     auth.login(request,user)
        return redirect('/customer/checkout/') 
        # else:
            
            # messages.info(request,'invalid credentials') 
            # return render(request, 'Customerlogin.html', context)  
    # else:
    #     return render(request, 'Customerlogin.html', context)
        
def register(request):
    categories=Category.objects.all()
    context={'categories':categories}         
    if request.method== "POST":
        username=request.POST['name']
        email=request.POST['email']
        gender=request.POST['gender']
        telephone=request.POST['tel']
        location=request.POST['Location']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if (password1==password2):
            if User.objects.filter(username=username).exists():
                print("username taken")
            elif User.objects.filter(email=email).exists(): 
                print("email taken")
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                getUser = User.objects.get(email=email)
                print(getUser)
                moredetails = MoreDetails.objects.create(user=getUser,gender=gender,telephone=telephone,location=location)
                moredetails.save()
        return redirect('/accounts/login/')     
    else:
        return render(request, 'register.html', context)  

def Alogin(request):
    categories=Category.objects.all()
    context={'categories':categories}         
    if request.method== "POST":
        return redirect('/dashboard/home/')      
    else:
        return render(request, 'login.html', context)
        
def Aregister(request):
    categories=Category.objects.all()
    context={'categories':categories}         
    if request.method== "POST":
        return redirect('/dashboard/login/')     
    else:
        return render(request, 'register.html', context)          
