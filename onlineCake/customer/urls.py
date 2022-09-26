
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_cart/', views.my_cart),
    path('category/<int:id>', views.category,),
    path('order_details/', views.order_details),
    path('product_details/', views.product_details),
    path('track_order/', views.track_order),
    path('track_orders/', views.track_orders), 
    path('checkout/', views.checkout), 
    path('likeIncrease/', views.likeIncrease),
    path('likeDecrease/', views.likeDecrease),    
    path('searchResults/', views.searchResults), 
    path('processOrder/', views.processOrder),      
    # path('updateItem/', views.UpdateItem),     
]
