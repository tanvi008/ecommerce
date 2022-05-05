from django.db import models
import uuid
from django.contrib.auth.models import User

#takes products which user wants to buy
class Product(models.Model):
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    productname = models.CharField(max_length=2000, null =True, blank=True)
    quantity = models.IntegerField(null= True, blank = True)

    # def __str__(self):
    #     return self.productname


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)

    # def __str__(self):
    #     return self.name

#stores details of all products
class Orders(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)


    
