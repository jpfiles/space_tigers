from django.db import models

# Create your models here.
class Product(models.Model):
   name = models.CharField(max_length=255)
   price = models.FloatField()
   stock = models.IntegerField()
   image_url = models.CharField(max_length=2083)

class Customer(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mi = models.CharField(max_length=1, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    avatar_url = models.URLField(blank=True)  

    def __str__(self):
        return f"{self.fname} {self.lname}"