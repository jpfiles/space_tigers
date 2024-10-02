from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin): 
  list_display = ('firstname', 'lastname', 'MI', 'email', 'phone', 'avatar', 'url') 
  
admin.site.register(Product)