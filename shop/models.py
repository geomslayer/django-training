from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название товара', null=False)
    price = models.CharField(max_length=300, verbose_name='Описание цены', null=False)
    description = models.TextField(verbose_name='Описание товара', null=False)
    image = models.ImageField(upload_to='products/', verbose_name='Сопровождающее фото', null=False)

    def __str__(self):
        return self.name
