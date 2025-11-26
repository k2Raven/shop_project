from django.db import models


class ProductOrder(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.RESTRICT, related_name='product_orders',
                                verbose_name='Товар')
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE, related_name='order_products',
                              verbose_name='Заказ')
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество')
