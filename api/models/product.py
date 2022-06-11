from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField()

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
