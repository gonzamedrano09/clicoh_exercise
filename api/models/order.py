from django.utils import timezone
from django.db import models
from api.models.product import Product


class Order(models.Model):
    date_time = models.DateTimeField(default=timezone.now)
    order_details = models.ManyToManyField(Product, through="OrderDetail")

    def __str__(self):
        return self.date_time
