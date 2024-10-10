from django.urls import path
from . import views
 
urlpatterns = [
   path('login/', views.login, name='login'),
   path('index/', views.index, name="index"),
   path('cust_list/', views.cust_list,name="cust_list"),
   path('newcustomer/', views.newcustomer, name="newcustomer"),
   path('contact_us/', views.contact_us, name="contact_us"),
]
