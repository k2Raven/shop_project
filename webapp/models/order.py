from django.db import models


class Order(models.Model):
    user_name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    number_phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    products = models.ManyToManyField('webapp.Product', through='webapp.ProductOrder',
                                      through_fields=('order', 'product'), related_name='orders',
                                      verbose_name='Продукты')
