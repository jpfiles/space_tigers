from django.contrib import admin 
from .models import Customer, Product 

# Register your models here. 
 

class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price', 'stock') 

    admin.site.register(Product)

class CustomerAdmin(admin.ModelAdmin): 
    list_display = ('lname', 'fname', 'mi', 'email', 'pnumber', 'ava_url') 

    admin.site.register(Customer)