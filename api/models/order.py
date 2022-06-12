from django.utils import timezone
from django.db import models
from api.models.product import Product


class Order(models.Model):

    date_time = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField(Product, through="OrderDetail")

    def __str__(self):
        return "Order N° %s" % str(self.id)
