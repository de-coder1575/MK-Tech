from itertools import product
from unicodedata import name
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Product, Customer, Order
from .serializers import *
from ecomapi import serializers
from .utils import updateProduct, getProductDetail, deleteProduct, getProductsList, createProduct, updateCustomer,getCustomerDetail,deleteCustomer,getCustomersList,createCustomer,updateOrder,getOrderDetail,getOrdersList,deleteOrder,createOrder
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/product/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Products'
        },
        {
            'Endpoint': '/product/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product object'
        },
        {
            'Endpoint': '/product/create/',
            'method': 'POST',
            'body': {'name': ""},
            'description': 'Creates new product with data sent in post request'
        },
        {
            'Endpoint': '/product/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing product with data sent in post request'
        },
        {
            'Endpoint': '/product/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting product'
        },


#customer
        {
            'Endpoint': '/customer/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Customers'
        },
        {
            'Endpoint': '/customer/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single customer object'
        },
        {
            'Endpoint': '/customer/create/',
            'method': 'POST',
            'body': {'name': ""},
            'description': 'Creates new customer with data sent in post request'
        },
        {
            'Endpoint': '/customer/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing customer with data sent in post request'
        },
        {
            'Endpoint': '/customer/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting customer'
        },
#order

        {
            'Endpoint': '/order/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Orders'
        },
        {
            'Endpoint': '/order/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single order object'
        },
        {
            'Endpoint': '/order/create/',
            'method': 'POST',
            'body': {'name': ""},
            'description': 'Creates new order with data sent in post request'
        },
        {
            'Endpoint': '/order/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing order with data sent in post request'
        },
        {
            'Endpoint': '/order/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting order'
        },
    ]
    return Response(routes)





@api_view(['GET', 'PUT', 'DELETE'])
def getProducts(request, pk):

    if request.method == 'GET':
        return getProductDetail(request, pk)

    if request.method == 'PUT':
        return updateProduct(request, pk)

    if request.method == 'DELETE':
        return deleteProduct(request, pk)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProduct(request):
     data = request.data
     product = Product.objects.create(
         body=data['body']
     )
     serializer = ProductSerializer(product, many=False)
     return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
     data = request.data
     product = Product.objects.get(id=pk)
     serializer = ProductSerializer(instance=product, data=data)

     if serializer.is_valid():
         serializer.save()

     return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteproduct(request, pk):
     product = Product.objects.get(id=pk)
     product.delete()
     return Response('Product was deleted!')




@permission_classes([IsAuthenticated])
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    
    #customers


@api_view(['GET', 'PUT', 'DELETE'])
def getCustomers(request, pk):

    if request.method == 'GET':
        return getCustomerDetail(request, pk)

    if request.method == 'PUT':
        return updateCustomer(request, pk)

    if request.method == 'DELETE':
        return deleteCustomer(request, pk)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCustomer(request):
     data = request.data
     customer = Customer.objects.create(
         body=data['body']
     )
     serializer = CustomerSerializer(customer, many=False)
     return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCustomer(request, pk):
     data = request.data
     customer = Customer.objects.get(id=pk)
     serializer = CustomerSerializer(instance=customer, data=data)

     if serializer.is_valid():
         serializer.save()

     return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletecustomer(request, pk):
     customer = Customer.objects.get(id=pk)
     customer.delete()
     return Response('Customer was deleted!')




@permission_classes([IsAdminUser])
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    


    #orders


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def getOrders(request, pk):

    if request.method == 'GET':
        return getOrderDetail(request, pk)

    if request.method == 'PUT':
        return updateOrder(request, pk)

    if request.method == 'DELETE':
        return deleteOrder(request, pk)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createOrder(request):
     data = request.data
     order = Order.objects.create(
         body=data['body']
     )
     serializer = OrderSerializer(order, many=False)
     return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrder(request, pk):
     data = request.data
     order = Order.objects.get(id=pk)
     serializer = OrderSerializer(instance=order, data=data)

     if serializer.is_valid():
         serializer.save()

     return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteOrder(request, pk):
     order = Order.objects.get(id=pk)
     order.delete()
     return Response('Order was deleted!')




@permission_classes([IsAdminUser])
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


#Admin

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def adminupdateOrder(request, pk):
     data = request.data
     order = Order.objects.get(id=pk)
     serializer = UpdateOrderSerializer(instance=order, data=data)

     if serializer.is_valid():
         serializer.save()

     return Response(serializer.data)