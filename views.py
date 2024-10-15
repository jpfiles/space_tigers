from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Customer
from .forms import CustomerForm  # Assuming you have a ModelForm for Customer

# Create your views here.

def login(request):
    return render(request, 'login.html')

def index(request):
    Product_list = Product.objects.all()
    return render(request, 'index.html', {'products': Product_list})

def cust_list(request):
    Customer_list = Customer.objects.all()
    return render(request, 'cust_list.html', {'customers': Customer_list})

def newcustomer(request):
    return render(request, 'newcustomer.html')

def contact_us(request):
    return render(request, 'contact_us.html')

# Update Customer
def update_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('cust_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'update_customer.html', {'form': form})

# Delete Customer
def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        customer.delete()
        return redirect('cust_list')
    return render(request, 'delete_confirm.html', {'object': customer})
