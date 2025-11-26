from django.urls import path
from webapp.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    AddProductToCartView, CartView, DeleteProductFromCartView, OrderCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),

    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/add_to_cart', AddProductToCartView.as_view(), name='product_add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<int:pk>/delete/', DeleteProductFromCartView.as_view(), name='cart_delete_product'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    # path('categories/add/', ProductCreateView.as_view(), name='category_add'),

]
