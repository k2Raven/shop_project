from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("Название"))
    description = models.TextField(null=True, blank=True, verbose_name=_('Описание'))
    category = models.ForeignKey('webapp.Category', on_delete=models.RESTRICT, related_name='products',
                                 verbose_name=_('Категория'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата и время добавления'))
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_('Стоимость'))
    image = models.URLField(verbose_name=_('Изображение'))
    balance = models.PositiveIntegerField(verbose_name=_('Остаток'), default=0)

    def __str__(self):
        return f'{self.id} - {self.title}'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})
