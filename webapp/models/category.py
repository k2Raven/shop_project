from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name=_('Название'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Описание'))

    def __str__(self):
        return f'{self.id} - {self.title}'
