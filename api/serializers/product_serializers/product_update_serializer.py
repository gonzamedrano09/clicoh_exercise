from rest_framework import serializers
from api.models.product import Product


class ProductUpdateSerializer(serializers.ModelSerializer):

    stock = serializers.IntegerField(read_only=True)
        
    class Meta:
        model = Product
        fields = ["id", "name", "price", "stock"]
