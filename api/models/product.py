from django.db import models
from api.managers.product_manager import ProductManager


class Product(models.Model):

    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField()

    is_deleted = models.BooleanField(default=False)

    all_objects = models.Manager()  # Manager for all products
    objects = ProductManager()  # Manager for non-removed products

    def __str__(self):
        return self.name
