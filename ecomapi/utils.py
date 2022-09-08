from typing import Any
from rest_framework.response import Response
from .models import Customer, Product, Order
from .serializers import *
#ProductSerializer, CustomerSerializer, OrderSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated



#Products

def getProductsList(request):
    products = Product.objects.all()
    #.order_by('-updated')
    serializer = ProductSerializer(products)
    return Response(serializer.data)


def getProductDetail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
def createProduct(request):
    data = request.data
    note = Product.objects.create(
        body=data['body']
    )
    serializer = ProductSerializer(note, many=False)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
def updateProduct(request, pk):
    data = request.data
    note = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data

@permission_classes([IsAuthenticated])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product was deleted!')




#Customers

def getCustomersList(request):
    customers = Customer.objects.all()
    #.order_by('-updated')
    serializer = CustomerSerializer(customers)
    return Response(serializer.data)


def getCustomerDetail(request, pk):
    customers = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customers, many=False)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
def createCustomer(request):
    data = request.data
    note = Customer.objects.create(
        body=data['body']
    )
    serializer = CustomerSerializer(note, many=False)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
def updateCustomer(request, pk):
    data = request.data
    note = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data

@permission_classes([IsAuthenticated])
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return Response('Customer was deleted!')





#Orders

def getOrdersList(request):
    orders = Order.objects.all()
    #.order_by('-updated')
    serializer = OrderSerializer(orders)
    return Response(serializer.data)


def getOrderDetail(request, pk):
    orders = Order.objects.get(id=pk)
    serializer = OrderSerializer(orders, many=False)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
def createOrder(request):
    data = request.data
    note = Order.objects.create(
        body=data['body']
    )
    serializer = OrderSerializer(note, many=False)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
def updateOrder(request, pk):
    data = request.data
    note = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data

@permission_classes([IsAuthenticated])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return Response('Order was deleted!')





#ADMIN


@permission_classes([IsAuthenticated])
def adminupdateOrder(request, pk):
    data = request.data
    note = Order.objects.get(id=pk)
    serializer = UpdateOrderSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data