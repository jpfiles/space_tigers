from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Customer
# Create your views here.
 
def login(request):
    return render(request, 'login.html')

def index(request):
    Product_list = Product.objects.all()
    return render(request, 'index.html', {'products': Product_list})

def cust_list(request):
    Customer_list = Customer.objects.all()
    return render(request, 'cust_list.html',{'customers': Customer_list})
 
def newcustomer(request):
    return render(request, 'newcustomer.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def new(request):
    return HttpResponse('New Page')
