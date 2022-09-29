
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login/', views.login),
    path('register/', views.register),
    path('Alogin/', views.Alogin),
    path('Aregister/', views.Aregister),    
    path('logout/', views.signout),  
]
