from django.db import models

# Create your models here.
from django.db.models import EmailField


class InfoPage(models.Model):
    price_page = models.IntegerField(verbose_name="Цена 1 схемы")
    phone_page = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.phone_page

    class Meta:
        verbose_name = 'Цена и телефон'
        verbose_name_plural = 'Цены и телефоны'


class StatusOrder(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_name = models.CharField(max_length=20, verbose_name='Имя')
    order_phone = models.CharField(max_length=20, verbose_name='Телефон')
    order_email = EmailField("Электронная почта", unique=False, max_length=255)
    order_organization_name = models.CharField("Название организации", max_length=255)
    order_organization_address = models.CharField("Адрес организации", max_length=255)
    order_count_images = models.IntegerField(verbose_name="Количество план-схем", blank=True)
    order_date_time = models.DateTimeField(verbose_name="Дата и время", auto_now=True)
    order_quantity = models.CharField(max_length=10, verbose_name='Итого')
    order_status = models.ForeignKey(StatusOrder, on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name='Статус')


    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
