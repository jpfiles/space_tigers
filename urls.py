from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('', views.index, name="index"),
    path('cust_list/', views.cust_list, name="cust_list"),
    path('newcustomer/', views.newcustomer, name="newcustomer"),
    path('contact_us/', views.contact_us, name="contact_us"),
    # New URLs for updating and deleting customers
    path('customer/update/<int:id>/', views.update_customer, name='update_customer'),
    path('customer/delete/<int:id>/', views.delete_customer, name='delete_customer'),
    path('cart/<int:id>', views.add_to_cart, name="add_to_cart"),
]
