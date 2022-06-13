import requests
from decimal import Decimal
from django.utils import timezone
from django.db import models
from api.models.product import Product


class Order(models.Model):

    date_time = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField(Product, through="OrderDetail")

    @property
    def get_total(self):
        total = 0
        for order_detail in self.order_details.all():
            total += order_detail.product.price * order_detail.quantity
        return Decimal(total).quantize(Decimal(".01"))

    @property
    def get_total_usd(self):
        try:
            dollar_list = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales").json()
        except Exception:
            dollar_list = []

        dollar_value = None
        for dollar in dollar_list:
            if dollar.get("casa").get("nombre") == "Dolar Blue":
                dollar_value = Decimal(dollar.get("casa").get("venta").replace(",", "."))
                break

        total_usd = None
        if dollar_value is not None:
            total_ars = self.get_total
            total_usd = total_ars / dollar_value
            
        return Decimal(total_usd).quantize(Decimal(".01")) if total_usd is not None else total_usd

    def __str__(self):
        return "Order N° %s" % str(self.id)
