from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

def index(request):
    return redirect('/accounts/Alogin/')

def home(request):
    return render(request, 'home.html')
        