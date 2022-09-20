
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('my_cart/', views.my_cart),
    path('category/', views.category),
    path('order_details/', views.order_details),
    path('product_details/', views.product_details),
    path('track_order/', views.track_order),
    path('track_orders/', views.track_orders),     
]
