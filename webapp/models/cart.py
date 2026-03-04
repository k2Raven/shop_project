from django.db import models
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='carts', verbose_name=_('Товар'))
    qty = models.PositiveIntegerField(verbose_name=_('Количество'), default=1)

    def get_total(self):
        return self.product.price * self.qty

    @classmethod
    def get_full_total_price(cls):
        return sum(cart.get_total() for cart in cls.objects.all())
