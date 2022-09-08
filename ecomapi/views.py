from itertools import product
from unicodedata import name
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Product, Customer, Order
from .serializers import ProductSerializer
from ecomapi import serializers
from .utils import updateProduct, getProductDetail, deleteProduct, getProductsList, createProduct


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
    ]
    return Response(routes)


# /notes GET
# /notes POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE

@api_view(['GET', 'POST'])
def getProducts(request):

    if request.method == 'GET':
        return getProductsList(request)

    if request.method == 'POST':
        return createProduct(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getProducts(request, pk):

    if request.method == 'GET':
        return getProductDetail(request, pk)

    if request.method == 'PUT':
        return updateProduct(request, pk)

    if request.method == 'DELETE':
        return deleteProduct(request, pk)


@api_view(['POST'])
def createProduct(request):
     data = request.data
     product = Product.objects.create(
         body=data['body']
     )
     serializer = ProductSerializer(product, many=False)
     return Response(serializer.data)


@api_view(['PUT'])
def updateProduct(request, pk):
     data = request.data
     product = Product.objects.get(id=pk)
     serializer = ProductSerializer(instance=product, data=data)

     if serializer.is_valid():
         serializer.save()

     return Response(serializer.data)


@api_view(['DELETE'])
def deleteproduct(request, pk):
     product = Product.objects.get(id=pk)
     product.delete()
     return Response('Product was deleted!')


