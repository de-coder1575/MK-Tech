from typing import Any
from rest_framework.response import Response
from .models import Customer, Product, Order
from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer


def getProductsList(request):
    products = Product.objects.all()
    #.order_by('-updated')
    serializer = ProductSerializer(products, many=Any)
    return Response(serializer.data)


def getProductDetail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


def createProduct(request):
    data = request.data
    note = Product.objects.create(
        body=data['body']
    )
    serializer = ProductSerializer(note, many=False)
    return Response(serializer.data)

def updateProduct(request, pk):
    data = request.data
    note = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product was deleted!')
