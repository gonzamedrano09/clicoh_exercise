from django.db import models
from api.models.product import Product
from api.models.order import Order


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cuantity = models.PositiveIntegerField()
