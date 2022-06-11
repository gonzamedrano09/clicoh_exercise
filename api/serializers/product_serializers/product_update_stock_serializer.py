from rest_framework import serializers
from api.models.product import Product


class ProductUpdateStockSerializer(serializers.ModelSerializer):

    name = serializers.CharField(read_only=True)
    price = serializers.DecimalField(max_digits=7, decimal_places=2, read_only=True)
        
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock"]
