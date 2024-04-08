from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Data_modified = models.DateTimeField(User, auto_now=True,)
    phone = models.CharField(max_length=50,blank = True)
    address1 = models.CharField(max_length=100,blank = True)
    address2 = models.CharField(max_length=100,blank = True)
    city = models.CharField(max_length=20,blank = True)
    state = models.CharField(max_length=20,blank = True)
    zipcode = models.CharField(max_length=20,blank = True)
    country = models.CharField(max_length=30,blank = True)
    old_cart = models.CharField(max_length=30,blank = True,null=True)


def create_profile(sender,instance,created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile,sender=User)

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=150,null=True,default='',blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/product/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2,default=0)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email =  models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    address = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    status = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True,blank=True)