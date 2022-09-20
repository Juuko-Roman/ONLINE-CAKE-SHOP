from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

def login(request):
    if request.method== "POST":
        return redirect('/customer/my_cart/')      
    else:
        return render(request, 'Customerlogin.html')
        
def register(request):
    if request.method== "POST":
        return redirect('/accounts/login')     
    else:
        return render(request, 'register.html')  
