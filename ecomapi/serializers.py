from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Product, Customer, Order


class ProductSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['name','picture1','picture2', 'stock']

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['user','products']        


class UpdateOrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__' 