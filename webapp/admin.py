from django.contrib import admin

from webapp.models import Category, Product, Cart, Order, ProductOrder

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(ProductOrder)

