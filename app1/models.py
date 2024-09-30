from django.db import models


from django.contrib.auth.models import User


from django.utils import timezone

# Create your models here.


class Products(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg')
    trending = models.BooleanField(default=0)
    offer = models.BooleanField(default=0)


class Cart(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    totalprice = models.IntegerField(default=0)
    host = models.ForeignKey(User,on_delete=models.CASCADE)


class Checkout(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    payment_method = [
        ('CC','Credit Card'),
        ('DC','Debit Card'),
        ('PP','PayPal'),
        ('COD','Cash On Delivery')
    ]

    payment = models.CharField(max_length=100,choices=payment_method)
    comments = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)


class Contact(models.Model):
    fname = models.CharField(max_length=100,verbose_name='First Name')
    lname = models.CharField(max_length=100,verbose_name='Last Name')
    email = models.CharField(max_length=100,verbose_name='Email Address')
    message = models.CharField(max_length=100,verbose_name='Message')

