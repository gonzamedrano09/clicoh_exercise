from rest_framework import serializers
from drf_extra_fields import relations
from api.models.order_detail import OrderDetail
from api.models.product import Product
from api.serializers.product_serializers.product_serializer import ProductSerializer


class OrderDetailSerializer(serializers.ModelSerializer):

    product = relations.PresentablePrimaryKeyRelatedField(queryset=Product.objects.all(),
                                                          presentation_serializer=ProductSerializer)

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("The quantity must be greater than 0.")
        return value

    def validate(self, data):
        if data.get("product").stock < data["quantity"]:
            raise serializers.ValidationError("There isn't enough stock of the product.")
        return data

    class Meta:
        model = OrderDetail
        fields = ["product", "quantity"]
