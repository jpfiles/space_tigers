from django.urls import path
from . import views
 
urlpatterns = [
   path('', views.index),
   path('new', views.new),
   path('table/', views.table),
   path('customer/', views.customer),
   path('contact_us/', views.contact_us),
]