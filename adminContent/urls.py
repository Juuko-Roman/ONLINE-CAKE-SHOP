from django.urls import path    
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('9/', views.dashboard, name='dashboard'),
    path('addpdt/', views.addpdt, name='addpdt'),
    path('reports/', views.reports, name='reports'),
    path('orders/', views.orders, name='orders'),
    path('transaction/', views.transaction, name='transaction'),
    path('customer/', views.customer, name='customer'),
    path('pdtlist/', views.pdtlist, name='pdtlist'),
    path('cat/', views.cat, name='cat'),
    
]