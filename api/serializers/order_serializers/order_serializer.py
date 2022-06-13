from rest_framework import serializers
from api.models.order import Order
from api.models.order_detail import OrderDetail
from api.serializers.order_detail_serializer.order_detail_serializer import OrderDetailSerializer


class OrderSerializer(serializers.ModelSerializer):

    order_details = OrderDetailSerializer(many=True)

    total = serializers.SerializerMethodField()
    total_usd = serializers.SerializerMethodField()

    def get_total(self, obj):
        return obj.get_total

    def get_total_usd(self, obj):
        return obj.get_total_usd

    def validate_order_details(self, value):
        if len(value) == 0:
            raise serializers.ValidationError("At least one order detail is needed.")

        products = []
        for order_detail in value:
            product = order_detail.get("product")
            if product in products:
                raise serializers.ValidationError("There can only be one order detail per product.")
            products.append(product)
        return value

    def create(self, validated_data):
        order_details_data = validated_data.pop("order_details")

        # Generate order
        order = Order.objects.create(**validated_data)

        # Generate order details
        for order_detail_data in order_details_data:
            order_detail = OrderDetail.objects.create(order=order, **order_detail_data)

            # Reduce the stock of products
            order_detail.product.stock -= order_detail.quantity
            order_detail.product.save()

        return order

    class Meta:
        model = Order
        fields = ["id", "date_time", "order_details", "total", "total_usd"]
