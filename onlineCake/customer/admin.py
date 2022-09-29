from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ShippingDetail)
admin.site.register(OrderItem)


# username = admin, email = admin@gmail.com, password = 1234