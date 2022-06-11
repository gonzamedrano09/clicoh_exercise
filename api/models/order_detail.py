from django.db import models
from api.models.product import Product
from api.models.order import Order


class OrderDetail(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "%s - %s" % (self.order.__str__(), self.order.__str__())
