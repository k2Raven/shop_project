from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.id} - {self.title}'
