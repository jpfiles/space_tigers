from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
 
def index(request):
    Product_list = Product.objects.all()
    return render(request, 'index.html', {'products': Product_list})
 
def customer(request):
    return render(request, 'customer.html')

def table(request):
    return render(request, 'table.html')

def contact_us(request):
    return render(request, 'cantact_us.html')

def new(request):
    return HttpResponse('New Page')