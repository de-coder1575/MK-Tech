from django.urls import path
from . import views
from .views import ProductList, CustomerList, OrderList


urlpatterns = [


#path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), # this view is to show the individual orders in our data base
#path('', PostList.as_view(), name='listcreate'), # this view is to show all the data(posts) in our data base


# this view is to show the individual products in our data base
#path('<int:pk>/', ProductDetail.as_view(), name='Proddetailcreate'),

# this view is to show the individual customers in our data base
#path('<int:pk>/', CustomerDetail.as_view(), name='Custdetailcreate'),

# this view is to show the individual orders in our data base

#path('<int:pk>/', OrderDetail.as_view(), name='Orderdetailcreate'),

#path('', ProductList.as_view(), name='Prodlistcreate'), # this view is to show all the Products in our data base
#path('', CustomerList.as_view(), name='Custlistcreate'), # this view is to show all the Customers in our data base
#path('', OrderList.as_view(), name='Ordrlistcreate'), # this view is to show all the orders in our data base

path('', views.getRoutes, name="routes"),

#Product URL's
path('products/', ProductList.as_view(), name='products'),

path('products/create/', views.createProduct, name="create-product"),
path('products/<str:pk>/update/', views.updateProduct, name="update-product"),
path('products/<str:pk>/delete/', views.deleteProduct, name="delete-product"),

path('products/<str:pk>/', views.getProducts, name="product"),


path('customers/', CustomerList.as_view(), name='customers'),

path('customers/create/', views.createCustomer, name="create-customer"),
path('customers/<str:pk>/update/', views.updateCustomer, name="update-customer"),
path('customers/<str:pk>/delete/', views.deleteCustomer, name="delete-customer"),

path('customers/<str:pk>/', views.getCustomers, name="customer"),


path('orders/', OrderList.as_view(), name='orders'),

path('orders/create/', views.createOrder, name="create-order"),
path('orders/<str:pk>/update/', views.updateOrder, name="update-order"),
path('orders/<str:pk>/delete/', views.deleteOrder, name="delete-order"),

path('orders/<str:pk>/', views.getOrders, name="order"),



path('orders/<str:pk>/adminupdate/', views.adminupdateOrder, name="admin-update-order"),




]