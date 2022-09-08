from django.urls import path
from . import views


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
path('products/', views.getProductsList, name="products"),
path('products/create/', views.createProduct, name="create-product"),
path('products/<str:pk>/update/', views.updateProduct, name="update-product"),
path('products/<str:pk>/delete/', views.deleteProduct, name="delete-product"),

path('products/<str:pk>/', views.getProducts, name="product"),


]