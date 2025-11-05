from django.urls import path
from webapp.views import product_list_view, product_create_view

urlpatterns = [
    path('', product_list_view, name='main'),
    path('products/', product_list_view, name='product_list'),
    path('products/add/', product_create_view, name='product_add'),
]
