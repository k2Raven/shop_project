from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user_name = models.CharField(max_length=100, verbose_name=_('Имя пользователя'))
    number_phone = models.CharField(max_length=20, verbose_name=_('Телефон'))
    address = models.CharField(max_length=100, verbose_name=_('Адрес'))
    products = models.ManyToManyField('webapp.Product', through='webapp.ProductOrder',
                                      through_fields=('order', 'product'), related_name='orders',
                                      verbose_name=_('Продукты'))
