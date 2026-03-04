from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductOrder(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.RESTRICT, related_name='product_orders',
                                verbose_name=_('Товар'))
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE, related_name='order_products',
                              verbose_name=_('Заказ'))
    qty = models.PositiveIntegerField(default=1, verbose_name=_('Количество'))
