from django.db import models

from django.contrib.auth.models import User

from ecom.models import Product

class order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    email = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=15500)
    amount_paid = models.DecimalField(max_digits=14, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
class OrderItem(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    order  = models.ForeignKey(order, on_delete=models.CASCADE)
    
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    price = models.DecimalField(max_digits=14, decimal_places=2)
    
    quantity = models.PositiveIntegerField(default=1)