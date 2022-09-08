from django.urls import path
from . import views
from .views import ProductList, CustomerList, OrderList


urlpatterns = [

path('', views.getRoutes, name="routes"),

#Product URL's
path('products/', ProductList.as_view(), name='products'),

path('products/create/', views.createProduct, name="create-product"),
path('products/<str:pk>/update/', views.updateProduct, name="update-product"),
path('products/<str:pk>/delete/', views.deleteProduct, name="delete-product"),

path('products/<str:pk>/', views.getProducts, name="product"),
path('product/<str:pk>/', views.getProduct, name="product"),


#Customer URL's

path('customers/', CustomerList.as_view(), name='customers'),

path('customers/create/', views.createCustomer, name="create-customer"),
path('customers/<str:pk>/update/', views.updateCustomer, name="update-customer"),
path('customers/<str:pk>/delete/', views.deleteCustomer, name="delete-customer"),

path('customers/<str:pk>/', views.getCustomers, name="customer"),


#Order URL's

path('orders/', OrderList.as_view(), name='orders'),

path('orders/create/', views.createOrder, name="create-order"),
path('orders/<str:pk>/update/', views.updateOrder, name="update-order"),
path('orders/<str:pk>/delete/', views.deleteOrder, name="delete-order"),

path('orders/<str:pk>/', views.getOrders, name="order"),



path('orders/<str:pk>/adminupdate/', views.adminupdateOrder, name="admin-update-order"),


]