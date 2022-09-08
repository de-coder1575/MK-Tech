from rest_framework.serializers import ModelSerializer
from .models import Product, Customer, Order


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'stock']

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'        