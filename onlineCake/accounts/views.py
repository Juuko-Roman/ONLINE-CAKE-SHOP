from contextvars import Context
from django.shortcuts import render, redirect
from customer.models import *

# Create your views here.

from django.http import HttpResponse

def login(request):
    categories=Category.objects.all()
    context={'categories':categories}         
    if request.method== "POST":
        return redirect('/customer/my_cart/')      
    else:
        return render(request, 'Customerlogin.html', context)
        
def register(request):
    categories=Category.objects.all()
    context={'categories':categories}         
    if request.method== "POST":
        return redirect('/accounts/login/')     
    else:
        return render(request, 'register.html', context)  
