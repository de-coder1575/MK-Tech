from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer


class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    picture1 = models.ImageField(upload_to='photos', max_length=254)
    picture2 = models.ImageField(upload_to='photos', max_length=254)
    stock = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name


STATUS_CHOICES = [
    ("Delivered", "Delivered"),
    ("Returned", "Returned"),
]

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    status = STATUS_CHOICES

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
